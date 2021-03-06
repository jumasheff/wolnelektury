# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from django import template
from catalogue.utils import split_tags
from ..engine import CustomCroppingEngine
import sorl.thumbnail.default
import logging

register = template.Library()

cropper = CustomCroppingEngine()

@register.inclusion_tag('picture/picture_wide.html', takes_context=True)
def picture_wide(context, picture):
    context.update({
        'picture': picture,
        'main_link': picture.get_absolute_url(),
        'request': context.get('request'),
        'tags': split_tags(picture.tags),
        })
    return context


@register.simple_tag()
def area_thumbnail_url(area, geometry):
    def to_square(coords):
        w = coords[1][0] - coords[0][0]
        h = coords[1][1] - coords[0][1]
        if w == h:
            return coords
        elif w > h:
            return [[coords[0][0] + w/2 - h/2, coords[0][1]],
                    [coords[1][0] - w/2 + h/2, coords[1][1]]]
        else:
            return [[coords[0][0], coords[0][1] + h/2 - w/2],
                    [coords[1][0], coords[1][1] - h/2 + w/2, ]]

    # so much for sorl extensibility.
    # what to do about this?
    _engine = sorl.thumbnail.default.engine
    sorl.thumbnail.default.engine = cropper
    coords = to_square(area.area)

    try:
        th = sorl.thumbnail.default.backend.get_thumbnail(
            area.picture.image_file,
            geometry,
            crop="%dpx %dpx %dpx %dpx" % tuple(map(lambda d: max(0, d), tuple(coords[0] + coords[1]))))
    except Exception, e:
        logging.exception("Error creating a thumbnail for PictureArea")
        return ''

    sorl.thumbnail.default.engine = _engine

    return th.url
