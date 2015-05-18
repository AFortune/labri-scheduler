# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0003_auto_20150413_1217'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Work',
            new_name='Job',
        ),
    ]
