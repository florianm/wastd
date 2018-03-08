# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0003_auto_20180219_1240'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taxon',
            options={'ordering': ['kingdom_id', 'family_nid', 'name_id'], 'verbose_name': 'Taxon', 'verbose_name_plural': 'Taxa'},
        ),
        migrations.AddField(
            model_name='taxon',
            name='ogc_fid',
            field=models.CharField(blank=True, help_text='The OCG Feature ID of the record, used to identify the record.', max_length=500, null=True, verbose_name='GeoServer OGC FeatureID'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='linear_sequence',
            field=models.TextField(blank=True, help_text='', null=True, verbose_name='Linear sequence'),
        ),
    ]
