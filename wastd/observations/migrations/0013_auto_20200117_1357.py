# Generated by Django 2.2.9 on 2020-01-17 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0012_lightsourceobservation_pathtosea_turtlehatchlingemergenceobservation_turtlehatchlingemergenceoutlier'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='label',
            field=models.CharField(blank=True, help_text='A human-readable, self-explanatory label.', max_length=500, null=True, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='lightsourceobservation',
            name='light_bearing_manual',
            field=models.FloatField(blank=True, help_text='.', null=True, verbose_name='Bearing'),
        ),
        migrations.AlterField(
            model_name='lightsourceobservation',
            name='light_source_type',
            field=models.CharField(choices=[('na', 'NA'), ('natural', 'Natural'), ('artificial', 'Artificial')], default='na', help_text='.', max_length=300, verbose_name='Light source type'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='bearing_to_water_manual',
            field=models.FloatField(blank=True, help_text='', null=True, verbose_name='Bearing to water'),
        ),
        migrations.AlterField(
            model_name='turtlehatchlingemergenceobservation',
            name='hatchling_path_to_sea',
            field=models.ManyToManyField(blank=True, related_name='path_to_sea', to='observations.PathToSea'),
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
            model_name='turtlehatchlingemergenceoutlierobservation',
            name='outlier_group_size',
            field=models.PositiveIntegerField(blank=True, help_text='', null=True, verbose_name='Number of tracks in outlier group'),
        ),
    ]