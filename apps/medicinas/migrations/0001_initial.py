# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-23 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aceites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre aceite')),
                ('resena', models.CharField(max_length=150, verbose_name='Rese\xf1a sobre el aceite')),
            ],
        ),
    ]