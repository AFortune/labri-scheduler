# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0013_day_info_dinner'),
    ]

    operations = [
        migrations.AddField(
            model_name='day_info',
            name='tasks',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
