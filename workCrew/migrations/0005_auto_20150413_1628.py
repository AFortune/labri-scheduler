# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0004_auto_20150413_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='arrivalDate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='student',
            name='departureDate',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
