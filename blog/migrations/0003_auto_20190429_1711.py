# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-29 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190425_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pv',
        ),
        migrations.RemoveField(
            model_name='post',
            name='uv',
        ),
    ]
