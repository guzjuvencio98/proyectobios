# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-26 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicinas', '0002_auto_20190526_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuidadocannabis',
            name='nombrep',
            field=models.CharField(default='value', max_length=15, verbose_name='Nombre Planta'),
        ),
    ]