# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators import cache

from catalogue.utils import get_random_hash
from catalogue.models import Book, Tag
from lesmianator.models import Poem, Continuations


def main_page(request):
    last = Poem.objects.all().order_by('-created_at')[:10]
    shelves = Tag.objects.filter(user__username='lesmianator')

    return render_to_response('lesmianator/lesmianator.html',
                {"last": last, "shelves": shelves},
                context_instance=RequestContext(request))


@cache.never_cache
def new_poem(request):
    user = request.user if request.user.is_authenticated() else None
    text = Poem.write()
    p = Poem(slug=get_random_hash(text), text=text, created_by=user)
    p.save()

    return render_to_response('lesmianator/poem.html',
                {"poem": p},
                context_instance=RequestContext(request))


@cache.never_cache
def poem_from_book(request, slug):
    book = get_object_or_404(Book, slug=slug)
    user = request.user if request.user.is_authenticated() else None
    text = Poem.write(Continuations.get(book))
    p = Poem(slug=get_random_hash(text), text=text, created_by=user)
    p.created_from = [book.id]
    p.save()

    return render_to_response('lesmianator/poem.html',
                {"poem": p, "books": [book], "book": book},
                context_instance=RequestContext(request))


@cache.never_cache
def poem_from_set(request, shelf):
    user = request.user if request.user.is_authenticated() else None
    tag = get_object_or_404(Tag, category='set', slug=shelf)
    text = Poem.write(Continuations.get(tag))
    p = Poem(slug=get_random_hash(text), text=text, created_by=user)
    books = Book.tagged.with_any((tag,))
    p.created_from = [b.id for b in books]
    p.save()

    book = books[0] if len(books) == 1 else None

    return render_to_response('lesmianator/poem.html',
                {"poem": p, "shelf": tag, "books": books, "book": book},
                context_instance=RequestContext(request))

def get_poem(request, poem):
    p = get_object_or_404(Poem, slug=poem)
    p.visit()
    if p.created_from:
        books = Book.objects.filter(id__in=p.created_from)
        book = books[0] if len(books) == 1 else None
    else:
        books = book = None

    return render_to_response('lesmianator/poem.html',
                {"poem": p, "books": books, "book": book},
                context_instance=RequestContext(request))


