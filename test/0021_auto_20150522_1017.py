# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0020_auto_20150518_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='day',
        ),
        migrations.AddField(
            model_name='job',
            name='days',
            field=models.ManyToManyField(to='workCrew.Day_Info', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='display_Name',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
