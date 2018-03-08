# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0004_auto_20180219_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxon',
            name='is_current',
            field=models.CharField(blank=True, help_text='WACensus currency status', max_length=100, null=True, verbose_name='Is name current?'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='linear_sequence',
            field=models.TextField(blank=True, help_text='', null=True, verbose_name='Linear sequence'),
        ),
    ]
