# Generated by Django 2.2.10 on 2020-03-05 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0015_auto_20200121_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='turtlenestencounter',
            name='eggs_counted',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='Was the nest excavated and were turtle eggs counted?', max_length=300, verbose_name='Nest excavated and eggs counted'),
        ),
        migrations.AddField(
            model_name='turtlenestencounter',
            name='fan_angles_measured',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='Were hatchling emergence track fan angles recorded?', max_length=300, verbose_name='Hatchling emergence recorded'),
        ),
        migrations.AddField(
            model_name='turtlenestencounter',
            name='hatchlings_measured',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='Were turtle hatchlings encountered and their morphometrics measured?', max_length=300, verbose_name='Hatchlings measured'),
        ),
        migrations.AddField(
            model_name='turtlenestencounter',
            name='logger_found',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='Was a data logger deployed, retrieved, or otherwise encountered?', max_length=300, verbose_name='Logger present'),
        ),
        migrations.AddField(
            model_name='turtlenestencounter',
            name='nest_tagged',
            field=models.CharField(choices=[('na', 'NA'), ('absent', 'Confirmed absent'), ('present', 'Confirmed present')], default='na', help_text='Was a nest tag applied, re-sighted, or otherwise encountered?', max_length=300, verbose_name='Nest tag present'),
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