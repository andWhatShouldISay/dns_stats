# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-07-25 21:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20190725_2104'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='uniqueid',
        ),
        migrations.RemoveField(
            model_name='domain',
            name='uniqueid',
        ),
        migrations.RemoveField(
            model_name='user',
            name='uniqueid',
        ),
    ]
