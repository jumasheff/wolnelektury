# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink, Q
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.files import File
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from newtagging.models import TagBase
from newtagging import managers

from librarian import html, dcparser


TAG_CATEGORIES = (
    ('author', _('author')),
    ('epoch', _('epoch')),
    ('kind', _('kind')),
    ('genre', _('genre')),
    ('theme', _('theme')),
    ('set', _('set')),
)


class TagSubcategoryManager(models.Manager):
    def __init__(self, subcategory):
        super(TagSubcategoryManager, self).__init__()
        self.subcategory = subcategory
        
    def get_query_set(self):
        return super(TagSubcategoryManager, self).get_query_set().filter(category=self.subcategory)


class Tag(TagBase):
    name = models.CharField(_('name'), max_length=50, unique=True, db_index=True)
    slug = models.SlugField(_('slug'), max_length=120, unique=True, db_index=True)
    sort_key = models.SlugField(_('sort key'), max_length=120, db_index=True)
    category = models.CharField(_('category'), max_length=50, blank=False, null=False, 
        db_index=True, choices=TAG_CATEGORIES)
    description = models.TextField(blank=True)
    
    user = models.ForeignKey(User, blank=True, null=True)
    
    def has_description(self):
        return len(self.description) > 0
    has_description.short_description = _('description')
    has_description.boolean = True

    @permalink
    def get_absolute_url(self):
        return ('catalogue.views.tagged_object_list', [self.slug])
    
    class Meta:
        ordering = ('sort_key',)
        verbose_name = _('tag')
        verbose_name_plural = _('tags')
    
    def __unicode__(self):
        return self.name

    @staticmethod
    def get_tag_list(tags):
        if isinstance(tags, basestring):
            tag_slugs = tags.split('/')
            return [Tag.objects.get(slug=slug) for slug in tag_slugs]
        else:
            return TagBase.get_tag_list(tags)


class Book(models.Model):
    title = models.CharField(_('title'), max_length=120)
    slug = models.SlugField(_('slug'), max_length=120, unique=True, db_index=True)
    description = models.TextField(_('description'), blank=True)
    created_at = models.DateTimeField(_('creation date'), auto_now=True)
    _short_html = models.TextField(_('short HTML'), editable=False)
    
    # Formats
    xml_file = models.FileField(_('XML file'), upload_to='books/xml', blank=True)
    pdf_file = models.FileField(_('PDF file'), upload_to='books/pdf', blank=True)
    odt_file = models.FileField(_('ODT file'), upload_to='books/odt', blank=True)
    html_file = models.FileField(_('HTML file'), upload_to='books/html', blank=True)
    
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')
    
    objects = models.Manager()
    tagged = managers.ModelTaggedItemManager(Tag)
    tags = managers.TagDescriptor(Tag)
    
    def short_html(self):
        if len(self._short_html):
            return mark_safe(self._short_html)
        else:
            tags = self.tags.filter(~Q(category__in=('set', 'theme')))
            tags = [u'<a href="%s">%s</a>' % (tag.get_absolute_url(), tag.name) for tag in tags]

            formats = []
            if self.html_file:
                formats.append(u'<a href="%s">Czytaj online</a>' % self.html_file.url)
            if self.pdf_file:
                formats.append(u'<a href="%s">Plik PDF</a>' % self.pdf_file.url)
            if self.odt_file:
                formats.append(u'<a href="%s">Plik ODT</a>' % self.odt_file.url)
            
            self._short_html = unicode(render_to_string('catalogue/book_short.html',
                {'book': self, 'tags': tags, 'formats': formats}))
            self.save()
            return mark_safe(self._short_html)
    
    def has_description(self):
        return len(self.description) > 0
    has_description.short_description = _('description')
    has_description.boolean = True
    
    def has_pdf_file(self):
        return bool(self.pdf_file)
    has_pdf_file.short_description = 'PDF'
    has_pdf_file.boolean = True
    
    def has_odt_file(self):
        return bool(self.odt_file)
    has_odt_file.short_description = 'ODT'
    has_odt_file.boolean = True
    
    def has_html_file(self):
        return bool(self.html_file)
    has_html_file.short_description = 'HTML'
    has_html_file.boolean = True

    @staticmethod
    def from_xml_file(xml_file):
        from tempfile import NamedTemporaryFile
        from slughifi import slughifi
        from markupstring import MarkupString
        
        # Read book metadata
        book_info = dcparser.parse(xml_file)
        book = Book(title=book_info.title, slug=slughifi(book_info.title))
        book.save()
        
        book_tags = []
        for category in ('kind', 'genre', 'author', 'epoch'):    
            tag_name = getattr(book_info, category)
            tag_sort_key = tag_name
            if category == 'author':
                tag_sort_key = tag_name.last_name
                tag_name = ' '.join(tag_name.first_names) + ' ' + tag_name.last_name
            tag, created = Tag.objects.get_or_create(name=tag_name,
                slug=slughifi(tag_name), sort_key=slughifi(tag_sort_key), category=category)
            tag.save()
            book_tags.append(tag)
        book.tags = book_tags
        
        if hasattr(book_info, 'parts'):
            for part_url in book_info.parts:
                base, slug = part_url.rsplit('/', 1)
                child_book = Book.objects.get(slug=slug)
                child_book.parent = book
                child_book.save()
        
        # Save XML and HTML files
        book.xml_file.save('%s.xml' % book.slug, File(file(xml_file)), save=False)
        
        html_file = NamedTemporaryFile()
        html.transform(book.xml_file.path, html_file)
        book.html_file.save('%s.html' % book.slug, File(html_file), save=False)
        
        # Extract fragments
        closed_fragments, open_fragments = html.extract_fragments(book.html_file.path)
        book_themes = []
        for fragment in closed_fragments.values():
            text = fragment.to_string()
            short_text = ''
            if (len(MarkupString(text)) > 240):
                short_text = unicode(MarkupString(text)[:160])
            new_fragment = Fragment(text=text, short_text=short_text, anchor=fragment.id, book=book)
                
            theme_names = [s.strip() for s in fragment.themes.split(',')]
            themes = []
            for theme_name in theme_names:
                tag, created = Tag.objects.get_or_create(name=theme_name,
                    slug=slughifi(theme_name), sort_key=slughifi(theme_name), category='theme')
                tag.save()
                themes.append(tag)
            new_fragment.save()
            new_fragment.tags = list(book.tags) + themes
            book_themes += themes
        
        book_themes = set(book_themes)
        book.tags = list(book.tags) + list(book_themes)
        return book.save()
    
    @permalink
    def get_absolute_url(self):
        return ('catalogue.views.book_detail', [self.slug])
        
    class Meta:
        ordering = ('title',)
        verbose_name = _('book')
        verbose_name_plural = _('books')

    def __unicode__(self):
        return self.title


class Fragment(models.Model):
    text = models.TextField()
    short_text = models.TextField(editable=False)
    _short_html = models.TextField(editable=False)
    anchor = models.CharField(max_length=120)
    book = models.ForeignKey(Book, related_name='fragments')

    objects = models.Manager()
    tagged = managers.ModelTaggedItemManager(Tag)
    tags = managers.TagDescriptor(Tag)
    
    def short_html(self):
        if len(self._short_html):
            return mark_safe(self._short_html)
        else:
            book_authors = [u'<a href="%s">%s</a>' % (tag.get_absolute_url(), tag.name) 
                for tag in self.book.tags if tag.category == 'author']
            
            self._short_html = unicode(render_to_string('catalogue/fragment_short.html',
                {'fragment': self, 'book': self.book, 'book_authors': book_authors}))
            self.save()
            return mark_safe(self._short_html)
        
    class Meta:
        ordering = ('book', 'anchor',)
        verbose_name = _('fragment')
        verbose_name_plural = _('fragments')
