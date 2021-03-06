# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from ajaxable.utils import AjaxableFormView

from catalogue.models import Book
from ssify import ssi_included
from social import forms
from .models import Cite
from social.utils import get_set, likes, set_sets


# ====================
# = Shelf management =
# ====================


@require_POST
def like_book(request, slug):
    if not request.user.is_authenticated():
        return HttpResponseForbidden('Login required.')
    book = get_object_or_404(Book, slug=slug)
    if not likes(request.user, book):
        tag = get_set(request.user, '')
        set_sets(request.user, book, [tag])

    if request.is_ajax():
        return JsonResponse({"success": True, "msg": "ok", "like": True})
    else:
        return redirect(book)


@login_required
def my_shelf(request):
    books = Book.tagged.with_any(request.user.tag_set.all())
    return render(request, 'social/my_shelf.html', locals())


class ObjectSetsFormView(AjaxableFormView):
    form_class = forms.ObjectSetsForm
    placeholdize = True
    template = 'social/sets_form.html'
    ajax_redirect = True
    POST_login = True

    def get_object(self, request, slug):
        return get_object_or_404(Book, slug=slug)

    def context_description(self, request, obj):
        return obj.pretty_title()

    def form_args(self, request, obj):
        return (obj, request.user), {}


@require_POST
def unlike_book(request, slug):
    if not request.user.is_authenticated():
        return HttpResponseForbidden('Login required.')
    book = get_object_or_404(Book, slug=slug)
    if likes(request.user, book):
        set_sets(request.user, book, [])

    if request.is_ajax():
        return JsonResponse({"success": True, "msg": "ok", "like": False})
    else:
        return redirect(book)


@ssi_included
def cite(request, pk, main=False):
    cite = get_object_or_404(Cite, pk=pk)
    return render(request, 'social/cite_promo.html', {
        'main': main,
        'cite': cite,
    })


@ssi_included(use_lang=False)
def cite_info(request, pk):
    cite = get_object_or_404(Cite, pk=pk)
    return render(request, 'social/cite_info.html', {
        'cite': cite,
    })
