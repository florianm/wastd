# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-08 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0104_auto_20171207_0909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loggerencounter',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='turtlenestencounter',
            name='comments',
        ),
        migrations.AddField(
            model_name='encounter',
            name='comments',
            field=models.TextField(blank=True, help_text='Comments', null=True, verbose_name='Comments'),
        ),
    ]