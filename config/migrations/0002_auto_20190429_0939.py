# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 01:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '友链', 'verbose_name_plural': '友链'},
        ),
    ]
