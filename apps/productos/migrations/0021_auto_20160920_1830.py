# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-20 23:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0020_auto_20160920_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='', max_length=200),
        ),
    ]