# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 06:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrazioni', '0005_auto_20151208_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrazione',
            name='impianto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='impianti.Impianto'),
            preserve_default=False,
        ),
    ]