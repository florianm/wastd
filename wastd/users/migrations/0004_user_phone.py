# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 00:12
from __future__ import unicode_literals

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20161013_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='The primary contact number.', max_length=128, null=True, verbose_name='Phone Number'),
        ),
    ]