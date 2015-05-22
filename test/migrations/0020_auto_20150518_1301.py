# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0019_auto_20150518_1252'),
    ]

    operations = [
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
    ]
