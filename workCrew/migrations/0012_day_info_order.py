# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0011_auto_20150505_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='day_info',
            name='order',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
