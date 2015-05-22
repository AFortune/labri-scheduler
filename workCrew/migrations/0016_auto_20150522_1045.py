# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0015_remove_day_info_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='day',
        ),
        migrations.RemoveField(
            model_name='job',
            name='helper_Name',
        ),
        migrations.AddField(
            model_name='day_info',
            name='breakfast',
            field=models.CharField(default=b'with', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helper',
            name='arrival_Date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helper',
            name='departure_Date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helper',
            name='jobs',
            field=models.ManyToManyField(to='workCrew.Job'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='days',
            field=models.ManyToManyField(to='workCrew.Day_Info', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_info',
            name='day',
            field=models.CharField(max_length=200, editable=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_info',
            name='dinner',
            field=models.CharField(default=b'with', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_info',
            name='lecture',
            field=models.CharField(default=b'none', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_info',
            name='order',
            field=models.IntegerField(default=b'0', editable=False),
            preserve_default=True,
        ),
    ]
