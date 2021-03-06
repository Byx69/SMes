# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 06:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registrazioni', '0003_auto_20151208_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrazione',
            name='evento',
            field=models.CharField(choices=[('ON', 'Impianto spento'), ('OFF', 'Impianto acceso'), ('ALS', 'Allarme scattato'), ('ALR', 'Allarme rientrato'), ('OP+', 'Operatore inserito'), ('OP-', 'Operatore disinserito')], max_length=3),
        ),
        migrations.AlterField(
            model_name='registrazione',
            name='impianto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='impianti.Impianto'),
        ),
        migrations.AlterField(
            model_name='registrazione',
            name='operatore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='operatori.Operatore'),
        ),
    ]
