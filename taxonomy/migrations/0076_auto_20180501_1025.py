# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 02:25
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0075_auto_20180420_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='eoo',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, help_text='The extent of occurrence as polygon in WGS84, if available.', null=True, srid=4326, verbose_name='Extent of Occurrence'),
        ),
        migrations.AddField(
            model_name='taxon',
            name='eoo',
            field=django.contrib.gis.db.models.fields.PolygonField(blank=True, help_text='The extent of occurrence as polygon in WGS84, if available.', null=True, srid=4326, verbose_name='Extent of Occurrence'),
        ),
        migrations.AlterField(
            model_name='hbvfamily',
            name='class_name',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='hbvfamily',
            name='division_name',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='Division'),
        ),
        migrations.AlterField(
            model_name='hbvfamily',
            name='family_name',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='Family Name'),
        ),
        migrations.AlterField(
            model_name='hbvfamily',
            name='kingdom_name',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='Kingdom'),
        ),
        migrations.AlterField(
            model_name='hbvfamily',
            name='order_name',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='Order Name'),
        ),
        migrations.AlterField(
            model_name='hbvfamily',
            name='supra_code',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='HBV Suprafamily Group Code'),
        ),
        migrations.AlterField(
            model_name='hbvgroup',
            name='class_id',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='HBV Suprafamily Group Code'),
        ),
        migrations.AlterField(
            model_name='hbvparent',
            name='class_id',
            field=models.CharField(blank=True, help_text='', max_length=100, null=True, verbose_name='WACensus ClassID'),
        ),
        migrations.AlterField(
            model_name='hbvspecies',
            name='consv_code',
            field=models.CharField(blank=True, help_text='', max_length=100, null=True, verbose_name='Conservation Code'),
        ),
        migrations.AlterField(
            model_name='hbvspecies',
            name='naturalised',
            field=models.CharField(blank=True, help_text='', max_length=100, null=True, verbose_name='Naturalised'),
        ),
        migrations.AlterField(
            model_name='hbvspecies',
            name='ranking',
            field=models.CharField(blank=True, help_text='', max_length=100, null=True, verbose_name='Ranking'),
        ),
        migrations.AlterField(
            model_name='hbvvernacular',
            name='name',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='hbvvernacular',
            name='vernacular',
            field=models.CharField(blank=True, help_text='', max_length=1000, null=True, verbose_name='Vernacular Name'),
        ),
    ]
