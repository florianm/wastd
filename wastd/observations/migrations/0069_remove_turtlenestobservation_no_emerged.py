# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 07:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0068_merge_20170201_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turtlenestobservation',
            name='no_emerged',
        ),
    ]
