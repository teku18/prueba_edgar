# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_prueba_alternativa'),
    ]

    operations = [
        migrations.AddField(
            model_name='prueba',
            name='alt',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
