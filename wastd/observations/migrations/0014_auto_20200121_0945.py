# Generated by Django 2.2.9 on 2020-01-21 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0013_auto_20200117_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lightsourceobservation',
            name='light_bearing_manual',
            field=models.FloatField(blank=True, help_text='Bearing captured with handheld compass.', null=True, verbose_name='Bearing'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='bearing_to_water_manual',
            field=models.FloatField(blank=True, help_text='Bearing captured with handheld compass.', null=True, verbose_name='Bearing to water'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='hatchling_emergence_time_source',
            field=models.CharField(blank=True, choices=[('na', 'NA'), ('same-night', 'Sometime that night'), ('plusminus-2h', 'Plusminus 2h of estimate'), ('plusminus-30m', 'Correct to the hour')], default='na', help_text='.', max_length=300, null=True, verbose_name='Hatchling emergence time estimate accuracy'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='leftmost_track_manual',
            field=models.FloatField(blank=True, help_text='Excluding outlier tracks, 5m from nest or at HWM. Bearing captured with handheld compass.', null=True, verbose_name='Leftmost track bearing of main fan'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='light_sources_present',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Light sources present during emergence'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='outlier_tracks_present',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='', max_length=300, verbose_name='Outlier tracks present'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='rightmost_track_manual',
            field=models.FloatField(blank=True, help_text='Excluding outlier tracks, 5m from nest or at HWM. Bearing captured with handheld compass.', null=True, verbose_name='Rightmost track bearing of main fan'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceoutlierobservation',
            name='outlier_group_size',
            field=models.PositiveIntegerField(blank=True, help_text='', null=True, verbose_name='Number of tracks in outlier group'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceoutlierobservation',
            name='outlier_track_bearing_manual',
            field=models.FloatField(blank=True, help_text='Aim at track 5m from nest or high water mark. Bearing captured with handheld compass.', null=True, verbose_name='Bearing'),
        ),
    ]
