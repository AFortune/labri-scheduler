# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0005_auto_20150413_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='arrivalDate',
            new_name='arrival_Date',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='departureDate',
            new_name='departure_Date',
        ),
    ]
