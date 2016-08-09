# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-09 00:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0003_auto_20160808_1703'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalencounter',
            name='habitat',
            field=models.CharField(choices=[('na', 'No habitat information available'), ('beach', 'B - Beach: Below the vegetation line of the grass slope'), ('bays-estuaries', 'BE - Bays, estuaries and other enclosed shallow soft sediments'), ('dune', 'D - Dune'), ('dune-constructed-hard-substrate', 'DC - Dune: Constructed hard substrate (concrete slabs, timber floors, helipad)'), ('dune-grass-area', 'DG - Dune: Grass area'), ('dune-compacted-path', 'DH - Dune: Hard compacted areas (road ways, paths)'), ('dune-rubble', 'DR - Dune: Rubble, usually coral'), ('dune-bare-sand', 'DS - Dune: Bare sand area'), ('dune-beneath-vegetation', 'DT - Dune: Beneath tree or shrub'), ('slope-front-dune', 'S - Slope: Front slope of dune'), ('sand-flats', 'SF - Sand flats'), ('slope-grass', 'SG - Slope: Grass area'), ('slope-bare-sand', 'SS - Slope: Bare sand area'), ('slope-beneath-vegetation', 'ST - Slope: Beneath tree or shrub'), ('below-mean-spring-high-water-mark', 'HW - Below the mean spring high water line or current level of inundation'), ('lagoon-patch-reef', 'LP - Lagoon: Patch reef'), ('lagoon-open-sand', 'LS - Lagoon: Open sand areas, typically shallow'), ('mangroves', 'M - Mangroves'), ('reef-coral', 'R - Reef: Coral reef'), ('reef-crest-front-slope', 'RC - Reef: Reef crest (dries at low water) and front reef slope areas'), ('reef-flat', 'RF - Reef: Reef flat, dries at low tide'), ('reef-seagrass-flats', 'RG - Coral reef with seagrass flats'), ('reef-rocky', 'RR - Reef: Rocky reef, e.g. adjacent to mainland'), ('open-water', 'OW - Open water, including inter reefal areas')], default='na', help_text='The habitat on which the animal was encountered.', max_length=500, verbose_name='Habitat'),
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