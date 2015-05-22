# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0018_auto_20150518_1241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='helper_Name',
        ),
        migrations.AddField(
            model_name='helper',
            name='jobs',
            field=models.ManyToManyField(to='workCrew.Job'),
            preserve_default=True,
        ),
    ]
