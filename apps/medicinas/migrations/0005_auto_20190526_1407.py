# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-26 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicinas', '0004_aceitecannabis_marca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aceitecannabis',
            name='marca',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='medicinas.Marcas'),
        ),
    ]
