# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Collection.title_de'
        db.add_column(u'catalogue_collection', 'title_de',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_en'
        db.add_column(u'catalogue_collection', 'title_en',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_es'
        db.add_column(u'catalogue_collection', 'title_es',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_fr'
        db.add_column(u'catalogue_collection', 'title_fr',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_it'
        db.add_column(u'catalogue_collection', 'title_it',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_lt'
        db.add_column(u'catalogue_collection', 'title_lt',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_pl'
        db.add_column(u'catalogue_collection', 'title_pl',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_ru'
        db.add_column(u'catalogue_collection', 'title_ru',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.title_uk'
        db.add_column(u'catalogue_collection', 'title_uk',
                      self.gf('django.db.models.fields.CharField')(blank=True, max_length=120, null=True, db_index=True),
                      keep_default=False)

        # Adding field 'Collection.description_de'
        db.add_column(u'catalogue_collection', 'description_de',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_en'
        db.add_column(u'catalogue_collection', 'description_en',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_es'
        db.add_column(u'catalogue_collection', 'description_es',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_fr'
        db.add_column(u'catalogue_collection', 'description_fr',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_it'
        db.add_column(u'catalogue_collection', 'description_it',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_lt'
        db.add_column(u'catalogue_collection', 'description_lt',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_pl'
        db.add_column(u'catalogue_collection', 'description_pl',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_ru'
        db.add_column(u'catalogue_collection', 'description_ru',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Collection.description_uk'
        db.add_column(u'catalogue_collection', 'description_uk',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_de'
        db.add_column(u'catalogue_tag', 'wiki_link_de',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_en'
        db.add_column(u'catalogue_tag', 'wiki_link_en',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_es'
        db.add_column(u'catalogue_tag', 'wiki_link_es',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_fr'
        db.add_column(u'catalogue_tag', 'wiki_link_fr',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_it'
        db.add_column(u'catalogue_tag', 'wiki_link_it',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_lt'
        db.add_column(u'catalogue_tag', 'wiki_link_lt',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_pl'
        db.add_column(u'catalogue_tag', 'wiki_link_pl',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_ru'
        db.add_column(u'catalogue_tag', 'wiki_link_ru',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Tag.wiki_link_uk'
        db.add_column(u'catalogue_tag', 'wiki_link_uk',
                      self.gf('django.db.models.fields.CharField')(max_length=240, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Collection.title_de'
        db.delete_column(u'catalogue_collection', 'title_de')

        # Deleting field 'Collection.title_en'
        db.delete_column(u'catalogue_collection', 'title_en')

        # Deleting field 'Collection.title_es'
        db.delete_column(u'catalogue_collection', 'title_es')

        # Deleting field 'Collection.title_fr'
        db.delete_column(u'catalogue_collection', 'title_fr')

        # Deleting field 'Collection.title_it'
        db.delete_column(u'catalogue_collection', 'title_it')

        # Deleting field 'Collection.title_lt'
        db.delete_column(u'catalogue_collection', 'title_lt')

        # Deleting field 'Collection.title_pl'
        db.delete_column(u'catalogue_collection', 'title_pl')

        # Deleting field 'Collection.title_ru'
        db.delete_column(u'catalogue_collection', 'title_ru')

        # Deleting field 'Collection.title_uk'
        db.delete_column(u'catalogue_collection', 'title_uk')

        # Deleting field 'Collection.description_de'
        db.delete_column(u'catalogue_collection', 'description_de')

        # Deleting field 'Collection.description_en'
        db.delete_column(u'catalogue_collection', 'description_en')

        # Deleting field 'Collection.description_es'
        db.delete_column(u'catalogue_collection', 'description_es')

        # Deleting field 'Collection.description_fr'
        db.delete_column(u'catalogue_collection', 'description_fr')

        # Deleting field 'Collection.description_it'
        db.delete_column(u'catalogue_collection', 'description_it')

        # Deleting field 'Collection.description_lt'
        db.delete_column(u'catalogue_collection', 'description_lt')

        # Deleting field 'Collection.description_pl'
        db.delete_column(u'catalogue_collection', 'description_pl')

        # Deleting field 'Collection.description_ru'
        db.delete_column(u'catalogue_collection', 'description_ru')

        # Deleting field 'Collection.description_uk'
        db.delete_column(u'catalogue_collection', 'description_uk')

        # Deleting field 'Tag.wiki_link_de'
        db.delete_column(u'catalogue_tag', 'wiki_link_de')

        # Deleting field 'Tag.wiki_link_en'
        db.delete_column(u'catalogue_tag', 'wiki_link_en')

        # Deleting field 'Tag.wiki_link_es'
        db.delete_column(u'catalogue_tag', 'wiki_link_es')

        # Deleting field 'Tag.wiki_link_fr'
        db.delete_column(u'catalogue_tag', 'wiki_link_fr')

        # Deleting field 'Tag.wiki_link_it'
        db.delete_column(u'catalogue_tag', 'wiki_link_it')

        # Deleting field 'Tag.wiki_link_lt'
        db.delete_column(u'catalogue_tag', 'wiki_link_lt')

        # Deleting field 'Tag.wiki_link_pl'
        db.delete_column(u'catalogue_tag', 'wiki_link_pl')

        # Deleting field 'Tag.wiki_link_ru'
        db.delete_column(u'catalogue_tag', 'wiki_link_ru')

        # Deleting field 'Tag.wiki_link_uk'
        db.delete_column(u'catalogue_tag', 'wiki_link_uk')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'catalogue.book': {
            'Meta': {'ordering': "('sort_key',)", 'object_name': 'Book'},
            '_related_info': ('jsonfield.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'changed_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'common_slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'cover': ('catalogue.fields.EbookField', [], {'max_length': '100', 'null': 'True', 'format_name': "'cover'", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'epub_file': ('catalogue.fields.EbookField', [], {'default': "''", 'max_length': '100', 'format_name': "'epub'", 'blank': 'True'}),
            'extra_info': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'fb2_file': ('catalogue.fields.EbookField', [], {'default': "''", 'max_length': '100', 'format_name': "'fb2'", 'blank': 'True'}),
            'gazeta_link': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'html_file': ('catalogue.fields.EbookField', [], {'default': "''", 'max_length': '100', 'format_name': "'html'", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'pol'", 'max_length': '3', 'db_index': 'True'}),
            'mobi_file': ('catalogue.fields.EbookField', [], {'default': "''", 'max_length': '100', 'format_name': "'mobi'", 'blank': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['catalogue.Book']"}),
            'parent_number': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'pdf_file': ('catalogue.fields.EbookField', [], {'default': "''", 'max_length': '100', 'format_name': "'pdf'", 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '120'}),
            'sort_key': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'txt_file': ('catalogue.fields.EbookField', [], {'default': "''", 'max_length': '100', 'format_name': "'txt'", 'blank': 'True'}),
            'wiki_link': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'xml_file': ('catalogue.fields.EbookField', [], {'default': "''", 'max_length': '100', 'format_name': "'xml'", 'blank': 'True'})
        },
        'catalogue.bookmedia': {
            'Meta': {'ordering': "('type', 'name')", 'object_name': 'BookMedia'},
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media'", 'to': "orm['catalogue.Book']"}),
            'extra_info': ('jsonfield.fields.JSONField', [], {'default': '{}'}),
            'file': ('catalogue.fields.OverwritingFileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'100'"}),
            'source_sha1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': "'100'", 'db_index': 'True'}),
            'uploaded_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'})
        },
        'catalogue.collection': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Collection'},
            'book_slugs': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_es': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_it': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_lt': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_pl': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_index': 'True'}),
            'title_de': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_es': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_fr': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_it': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_lt': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_pl': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '120', 'null': True, 'db_index': 'True'})
        },
        'catalogue.fragment': {
            'Meta': {'ordering': "('book', 'anchor')", 'object_name': 'Fragment'},
            'anchor': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fragments'", 'to': "orm['catalogue.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_text': ('django.db.models.fields.TextField', [], {}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'catalogue.tag': {
            'Meta': {'ordering': "('sort_key',)", 'unique_together': "(('slug', 'category'),)", 'object_name': 'Tag'},
            'book_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'changed_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'db_index': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description_de': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_es': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_fr': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_it': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_lt': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_pl': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_ru': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': True, 'blank': True}),
            'gazeta_link': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'name_de': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_en': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_es': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_fr': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_it': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_lt': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_pl': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_ru': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'name_uk': ('django.db.models.fields.CharField', [], {'blank': True, 'max_length': '50', 'null': True, 'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'sort_key': ('django.db.models.fields.CharField', [], {'max_length': '120', 'db_index': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'wiki_link': ('django.db.models.fields.CharField', [], {'max_length': '240', 'blank': 'True'}),
            'wiki_link_de': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_en': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_es': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_fr': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_it': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_lt': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_pl': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_ru': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True}),
            'wiki_link_uk': ('django.db.models.fields.CharField', [], {'max_length': '240', 'null': True, 'blank': True})
        },
        'catalogue.tagrelation': {
            'Meta': {'unique_together': "(('tag', 'content_type', 'object_id'),)", 'object_name': 'TagRelation', 'db_table': "u'catalogue_tag_relation'"},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['catalogue.Tag']"})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['catalogue']