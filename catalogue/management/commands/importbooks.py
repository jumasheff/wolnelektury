from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import color_style
from optparse import make_option
import sys
import os

from catalogue.lib.dcparser import parse
from catalogue.lib.slughifi import slughifi
from catalogue.models import Book, Tag


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--verbosity', action='store', dest='verbosity', default='1',
            type='choice', choices=['0', '1', '2'],
            help='Verbosity level; 0=minimal output, 1=normal output, 2=all output'),
    )
    help = 'Imports books from the specified directories.'
    args = 'directory [directory ...]'

    def handle(self, *directories, **options):
        from django.db import transaction

        self.style = color_style()

        verbosity = int(options.get('verbosity', 1))
        show_traceback = options.get('traceback', False)

        # Start transaction management.
        transaction.commit_unless_managed()
        transaction.enter_transaction_management()
        transaction.managed(True)

        for dir_name in directories:
            if not os.path.isdir(dir_name):
                print self.style.ERROR("Skipping '%s': not a directory." % dir_name)
            else:
                for file_name in os.listdir(dir_name):
                    file_path = os.path.join(dir_name, file_name)
                    if not os.path.splitext(file_name)[1] == '.xml':
                        print self.style.NOTICE("Skipping '%s': not an XML file." % file_path)
                        continue
                    if verbosity > 1:
                        print "Parsing '%s'" % file_path
                        
                    book_info = parse(file_path)
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
        
        
        transaction.commit()
        transaction.leave_transaction_management()

