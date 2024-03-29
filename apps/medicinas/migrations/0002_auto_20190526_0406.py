# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-26 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicinas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AceiteCannabis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre aceite')),
                ('resena', models.TextField(max_length=150, verbose_name='Rese\xf1a sobre el aceite')),
                ('mdu', models.TextField(max_length=150, verbose_name='Modo de uso')),
                ('ES', models.CharField(max_length=150, verbose_name='Efectos secundarios')),
                ('Precio', models.CharField(max_length=10, verbose_name='Precio')),
                ('Importador', models.CharField(max_length=20, verbose_name='Importador')),
            ],
        ),
        migrations.CreateModel(
            name='CremaCannabis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resena', models.TextField(max_length=150, verbose_name='Rese\xf1a sobre la crema')),
                ('mdu', models.TextField(max_length=100, verbose_name='Modo de uso')),
                ('ES', models.CharField(max_length=10, verbose_name='Efectos secundarios')),
                ('Precio', models.CharField(max_length=5, verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='CuidadoCannabis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metodo', models.CharField(max_length=15, verbose_name='Metodo')),
                ('ambiente', models.CharField(max_length=15, verbose_name='Ambiente mas favorable')),
                ('productos', models.CharField(max_length=15, verbose_name='productos que puede utilizar')),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, verbose_name='Marca')),
            ],
        ),
        migrations.CreateModel(
            name='ParcheCannabis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resena', models.TextField(max_length=150, verbose_name='Rese\xf1a sobre el parche')),
                ('mdu', models.TextField(max_length=100, verbose_name='Modo de uso')),
                ('ES', models.CharField(max_length=10, verbose_name='Efectos secundarios')),
                ('Precio', models.CharField(max_length=5, verbose_name='Precio')),
            ],
        ),
        migrations.CreateModel(
            name='PastillaCannabis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre pastilla')),
                ('resena', models.TextField(max_length=150, verbose_name='Rese\xf1a sobre la pastilla')),
                ('mdu', models.TextField(max_length=150, verbose_name='Modo de uso')),
                ('ES', models.CharField(max_length=150, verbose_name='Efectos secundarios')),
                ('Precio', models.CharField(max_length=10, verbose_name='Precio')),
                ('Importador', models.CharField(max_length=20, verbose_name='Importador')),
            ],
        ),
        migrations.CreateModel(
            name='PlantaMasticable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre planta')),
                ('resena', models.TextField(max_length=150, verbose_name='Rese\xf1a sobre la planta')),
                ('mdu', models.TextField(max_length=150, verbose_name='Modo de uso')),
                ('ES', models.CharField(max_length=150, verbose_name='Efectos secundarios')),
                ('Precio', models.CharField(max_length=10, verbose_name='Precio')),
                ('Importador', models.CharField(max_length=20, verbose_name='Importador')),
            ],
        ),
        migrations.DeleteModel(
            name='aceites',
        ),
    ]
