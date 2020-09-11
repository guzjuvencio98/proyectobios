# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AceiteCannabis, CremaCannabis, ParcheCannabis, PlantaMasticable, PastillaCannabis, Marcas, CuidadoCannabis

admin.site.register(CuidadoCannabis)
admin.site.register(Marcas)
admin.site.register(PlantaMasticable)
admin.site.register(AceiteCannabis)
admin.site.register(CremaCannabis)
admin.site.register(ParcheCannabis)
admin.site.register(PastillaCannabis)
# Register your models here.
