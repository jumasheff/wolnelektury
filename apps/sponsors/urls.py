# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django.conf.urls import patterns, url

urlpatterns = patterns('sponsors.views',
    url(r'^page/(?P<name>.+)\.html$', 'page', name='sponsor_page'),
)
