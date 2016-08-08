# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-08 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0002_auto_20160808_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='CetaceanEncounter',
            fields=[
                ('animalencounter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='observations.AnimalEncounter')),
            ],
            options={
                'ordering': ['when', 'where'],
                'get_latest_by': 'when',
                'verbose_name': 'Cetacean Encounter',
                'verbose_name_plural': 'Cetacean Encounters',
            },
            bases=('observations.animalencounter',),
        ),
        migrations.AlterField(
            model_name='distinguishingfeatureobservation',
            name='algal_growth',
            field=models.CharField(choices=[('na', 'Not observed'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Algal growth on carapace'),
        ),
        migrations.AlterField(
            model_name='distinguishingfeatureobservation',
            name='barnacles',
            field=models.CharField(choices=[('na', 'Not observed'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Barnacles'),
        ),
        migrations.AlterField(
            model_name='distinguishingfeatureobservation',
            name='damage_injury',
            field=models.CharField(choices=[('na', 'Not observed'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Obvious damage or injuries'),
        ),
        migrations.AlterField(
            model_name='distinguishingfeatureobservation',
            name='missing_limbs',
            field=models.CharField(choices=[('na', 'Not observed'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Missing limbs'),
        ),
        migrations.AlterField(
            model_name='distinguishingfeatureobservation',
            name='propeller_damage',
            field=models.CharField(choices=[('na', 'Not observed'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Propeller strike damage'),
        ),
        migrations.AlterField(
            model_name='distinguishingfeatureobservation',
            name='scanned_for_pit_tags',
            field=models.CharField(choices=[('na', 'Not observed'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Scanned for PIT tags'),
        ),
        migrations.AlterField(
            model_name='distinguishingfeatureobservation',
            name='tagging_scars',
            field=models.CharField(choices=[('na', 'Not observed'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Tagging scars'),
        ),
    ]
