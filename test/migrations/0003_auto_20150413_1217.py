# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0002_auto_20150413_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helper',
            name='contact_info',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='contact_info',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='workNote',
            field=models.ForeignKey(blank=True, to='workCrew.WorkNote', null=True),
            preserve_default=True,
        ),
    ]
