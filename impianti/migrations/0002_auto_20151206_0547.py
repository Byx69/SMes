# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-06 05:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('impianti', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='impianto',
            options={'ordering': ['codice'], 'verbose_name': 'impianto', 'verbose_name_plural': 'impianti'},
        ),
    ]
