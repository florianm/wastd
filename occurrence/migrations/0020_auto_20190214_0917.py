# Generated by Django 2.1.7 on 2019-02-14 01:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('occurrence', '0019_auto_20190213_2011'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='associatedspeciesobservation',
            options={'verbose_name': 'Associated Species', 'verbose_name_plural': 'Associated Species'},
        ),
        migrations.AlterModelOptions(
            name='firehistoryobservation',
            options={'verbose_name': 'Fire History', 'verbose_name_plural': 'Fire Histories'},
        ),
        migrations.AlterField(
            model_name='areaencounter',
            name='source_id',
            field=models.CharField(default=uuid.UUID('413eb9e2-2ff6-11e9-a86f-40f02f6195e0'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
        migrations.AlterField(
            model_name='observationgroup',
            name='encounter',
            field=models.ForeignKey(help_text='The Area Encounter during which the observation group was observed.', on_delete=django.db.models.deletion.CASCADE, related_name='observations', to='occurrence.AreaEncounter', verbose_name='Area Encounter'),
        ),
    ]
