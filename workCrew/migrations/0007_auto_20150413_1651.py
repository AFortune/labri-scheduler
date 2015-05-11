# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0006_auto_20150413_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='helper',
            old_name='firstName',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='helper',
            old_name='lastName',
            new_name='last_Name',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='crewSize',
            new_name='crew_Size',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='helperName',
            new_name='helper_Name',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='workName',
            new_name='work_Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='firstName',
            new_name='first_Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='lastName',
            new_name='last_Name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='workNote',
            new_name='work_Note',
        ),
    ]
