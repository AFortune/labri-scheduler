# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0021_auto_20150522_1017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='crew_Size',
        ),
        migrations.RemoveField(
            model_name='job',
            name='days',
        ),
        migrations.RemoveField(
            model_name='job',
            name='display_Name',
        ),
    ]
