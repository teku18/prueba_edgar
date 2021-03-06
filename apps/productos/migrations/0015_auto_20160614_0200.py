# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-14 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0014_estatu_marca'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estatus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.estatu'),
        ),
        migrations.AddField(
            model_name='producto',
            name='marcas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.marca'),
        ),
    ]
