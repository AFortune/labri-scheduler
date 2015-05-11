# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0007_auto_20150413_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_Name', models.CharField(max_length=200)),
                ('last_Name', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
