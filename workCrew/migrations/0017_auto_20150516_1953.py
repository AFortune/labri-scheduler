# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0016_auto_20150516_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='day_info',
            name='day',
            field=models.CharField(max_length=200, editable=False),
            preserve_default=True,
        ),
    ]
