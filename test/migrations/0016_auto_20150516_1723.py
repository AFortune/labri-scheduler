# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0015_remove_day_info_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='day_info',
            name='breakfast',
            field=models.CharField(default=b'with', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_info',
            name='dinner',
            field=models.CharField(default=b'with', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_info',
            name='lecture',
            field=models.CharField(default=b'none', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='day_info',
            name='order',
            field=models.IntegerField(default=b'0', editable=False),
            preserve_default=True,
        ),
    ]
