# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-14 06:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0010_auto_20160607_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='caducidad',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='estatus',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]