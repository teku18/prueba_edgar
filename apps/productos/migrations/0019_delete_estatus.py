# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-22 19:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0018_auto_20160621_0024'),
    ]

    operations = [
        migrations.DeleteModel(
            name='estatus',
        ),
    ]