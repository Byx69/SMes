# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrazioni', '0007_auto_20151208_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrazione',
            name='evento',
            field=models.CharField(choices=[('ON', 'Impianto spento'), ('OFF', 'Impianto acceso'), ('ALS', 'Allarme scattato'), ('ALR', 'Allarme rientrato'), ('OP+', 'Operatore inserito'), ('OP-', 'Operatore disinserito'), ('ORA', 'Ordine aperto'), ('ORO', 'Ordine chiuso'), ('PRO', 'Produzione')], max_length=3),
        ),
    ]
