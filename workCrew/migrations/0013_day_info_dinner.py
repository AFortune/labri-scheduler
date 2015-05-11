# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0012_day_info_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='day_info',
            name='dinner',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
