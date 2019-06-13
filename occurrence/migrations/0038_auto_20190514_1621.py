# Generated by Django 2.1.7 on 2019-05-14 08:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('occurrence', '0037_auto_20190514_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='areaencounter',
            name='area_type',
            field=models.PositiveIntegerField(choices=[(0, 'Fauna Ephemeral Site'), (1, 'Fauna Permanent Site'), (3, 'Generic Partial survey'), (2, 'Critical Habitat'), (10, 'TEC Boundary'), (11, 'TEC Buffer'), (12, 'TEC Site'), (20, 'Flora Population'), (21, 'Flora Subpopulation'), (30, 'Fauna Site'), (40, 'Marine Protected Area'), (41, 'Locality')], default=0, help_text='What type describes the area occupied by the encounter most accurately? The area can be an opportunistic, once-off chance encounter (point), a fixed survey site (polygon), a partial or a complete survey of an area occupied by the encountered subject (polygon).', verbose_name='Area type'),
        ),
        migrations.AlterField(
            model_name='areaencounter',
            name='source_id',
            field=models.CharField(default=uuid.UUID('45d1ec6a-7621-11e9-a870-ecf4bb19b5fc'), help_text='The ID of the record in the original source, if available.', max_length=1000, verbose_name='Source ID'),
        ),
    ]