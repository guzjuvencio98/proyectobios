# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-26 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicinas', '0007_remove_aceitecannabis_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuidadocannabis',
            name='nombrep',
            field=models.CharField(max_length=15, verbose_name='Nombre Planta'),
        ),
    ]