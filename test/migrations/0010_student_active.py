# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0009_day_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='active',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
