# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0014_day_info_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day_info',
            name='tasks',
        ),
    ]
