# -*- coding: utf-8 -*-
# This file is part of Wolnelektury, licensed under GNU Affero GPLv3 or later.
# Copyright © Fundacja Nowoczesna Polska. See NOTICE for more information.
#
from decimal import Decimal
from django import forms
from django.template.loader import render_to_string


class PerksAmountWidget(forms.Textarea):
    def perks_input_name(self, name):
        return "_%s_perk" % name

    def render(self, name, value, attrs=None):
        try:
            value = Decimal(value)
        except:
            pass
        perks = list(self.form_instance.offer.get_perks())
        perk_chosen = False
        for perk in perks:
            if perk.price == value:
                perk.chosen = True
                perk_chosen = True
                break

        return render_to_string("funding/widgets/amount.html", {
                "perks": perks,
                "name": name,
                "perks_input_name": self.perks_input_name(name),
                "perk_chosen": perk_chosen,
                "value": value,
                "attrs": attrs,
            })

    def value_from_datadict(self, data, files, name):
        num_str = data.get(self.perks_input_name(name)) or data[name]
        return num_str.replace(',', '.')
