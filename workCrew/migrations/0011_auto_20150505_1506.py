# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0010_student_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='day',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='job',
            name='time',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
    ]
