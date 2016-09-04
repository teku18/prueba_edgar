# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 23:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='prueba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palabra', models.CharField(default='', max_length=30)),
                ('preguntas', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='nombre',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]