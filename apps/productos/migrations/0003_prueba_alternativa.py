# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20160602_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='alternativa',
            field=models.CharField(default='', max_length=30),
        ),
    ]
