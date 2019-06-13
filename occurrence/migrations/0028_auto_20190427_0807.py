# Generated by Django 2.1.7 on 2019-04-27 00:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('occurrence', '0027_auto_20190426_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='EncounterType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(help_text='A unique, url-safe code.', max_length=500, unique=True, verbose_name='Code')),
                ('label', models.CharField(blank=True, help_text='A human-readable, self-explanatory label.', max_length=500, null=True, verbose_name='Label')),
                ('description', models.TextField(blank=True, help_text='A comprehensive description.', null=True, verbose_name='Description')),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SurveyMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(help_text='A unique, url-safe code.', max_length=500, unique=True, verbose_name='Code')),
                ('label', models.CharField(blank=True, help_text='A human-readable, self-explanatory label.', max_length=500, null=True, verbose_name='Label')),
                ('description', models.TextField(blank=True, help_text='A comprehensive description.', null=True, verbose_name='Description')),
            ],
            options={
                'ordering': ['code'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='habitatcondition',
            name='observationgroup_ptr',
        ),
        migrations.AlterField(
            model_name='areaencounter',
            name='source_id',
            field=models.CharField(default=uuid.UUID('5e3a7e6a-6880-11e9-a870-40f02f6195e0'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
        migrations.DeleteModel(
            name='HabitatCondition',
        ),
        migrations.AddField(
            model_name='areaassessment',
            name='survey_method',
            field=models.ForeignKey(blank=True, help_text='Add missing survey methods via the data curation portal.', null=True, on_delete=django.db.models.deletion.CASCADE, to='occurrence.SurveyMethod', verbose_name='Survey Method'),
        ),
        migrations.AddField(
            model_name='areaencounter',
            name='encounter_type',
            field=models.ForeignKey(blank=True, help_text='Add missing encounter types via the data curation portal.', null=True, on_delete=django.db.models.deletion.CASCADE, to='occurrence.EncounterType', verbose_name='Encounter Type'),
        ),
    ]