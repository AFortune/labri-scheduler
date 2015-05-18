# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0017_auto_20150516_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='helper_Name',
            field=models.ForeignKey(default=1, to='workCrew.Helper'),
            preserve_default=True,
        ),
    ]
