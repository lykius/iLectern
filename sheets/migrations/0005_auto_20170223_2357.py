# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 22:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0004_sheet_number_of_pages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sheet',
            name='file_name',
        ),
        migrations.RemoveField(
            model_name='sheet',
            name='number_of_pages',
        ),
    ]