# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 06:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0045_auto_20161110_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracktallyobservation',
            name='track_type',
            field=models.CharField(choices=[('old-track', 'old track, unsure if false or successful'), ('new-track', 'new track, unsure if false of successful'), ('old-track-false-crawl', 'old false crawl'), ('old-track-false-crawl', 'old successful crawl'), ('new-track-false-crawl', 'new false crawl'), ('new-track-successful-crawl', 'new successful crawl'), ('nesting-turtle-present', 'new nest turtle present'), ('fresh', 'new nest turtle absent'), ('predated', 'predated nest'), ('hatched', 'hatched nest')], default='new-track-successful-crawl', help_text='The nest age and type.', max_length=300, verbose_name='Track type'),
        ),
        migrations.AlterField(
            model_name='turtlenestencounter',
            name='comments',
            field=models.TextField(blank=True, help_text='Comments', null=True, verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='turtlenestencounter',
            name='nest_age',
            field=models.CharField(choices=[('old-track', 'old track, unsure if false or successful'), ('new-track', 'new track, unsure if false of successful'), ('old-track-false-crawl', 'old false crawl'), ('old-track-false-crawl', 'old successful crawl'), ('new-track-false-crawl', 'new false crawl'), ('new-track-successful-crawl', 'new successful crawl'), ('nesting-turtle-present', 'new nest turtle present'), ('fresh', 'new nest turtle absent'), ('predated', 'predated nest'), ('hatched', 'hatched nest')], default='new', help_text='The track or nest age and type.', max_length=300, verbose_name='Nest age'),
        ),
    ]
