# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-05 02:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conservation', '0009_auto_20180405_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='communitygazettal',
            name='label_cache',
            field=models.TextField(blank=True, help_text='An auto-generated label for the Gazettal minus the Taxon.', null=True, verbose_name='Gazettal label'),
        ),
        migrations.AddField(
            model_name='taxongazettal',
            name='label_cache',
            field=models.TextField(blank=True, help_text='An auto-generated label for the Gazettal minus the Taxon.', null=True, verbose_name='Gazettal label'),
        ),
        migrations.AlterField(
            model_name='communitygazettal',
            name='category_cache',
            field=models.TextField(blank=True, help_text='An auto-generated list of conservation categories.', null=True, verbose_name='Category list'),
        ),
        migrations.AlterField(
            model_name='communitygazettal',
            name='community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='community_gazettal', to='taxonomy.Community'),
        ),
        migrations.AlterField(
            model_name='communitygazettal',
            name='criteria',
            field=models.ManyToManyField(blank=True, help_text='The Conservation Criteria form the reason for the choice of conservation categories.', to='conservation.ConservationCriterion', verbose_name='Conservation Criteria'),
        ),
        migrations.AlterField(
            model_name='communitygazettal',
            name='criteria_cache',
            field=models.TextField(blank=True, help_text='An auto-generated list of conservation criteria.', null=True, verbose_name='Criteria list'),
        ),
        migrations.AlterField(
            model_name='taxongazettal',
            name='category_cache',
            field=models.TextField(blank=True, help_text='An auto-generated list of conservation categories.', null=True, verbose_name='Category list'),
        ),
        migrations.AlterField(
            model_name='taxongazettal',
            name='criteria',
            field=models.ManyToManyField(blank=True, help_text='The Conservation Criteria form the reason for the choice of conservation categories.', to='conservation.ConservationCriterion', verbose_name='Conservation Criteria'),
        ),
        migrations.AlterField(
            model_name='taxongazettal',
            name='criteria_cache',
            field=models.TextField(blank=True, help_text='An auto-generated list of conservation criteria.', null=True, verbose_name='Criteria list'),
        ),
        migrations.AlterField(
            model_name='taxongazettal',
            name='taxon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taxon_gazettal', to='taxonomy.Taxon'),
        ),
    ]