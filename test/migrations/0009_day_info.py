# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0008_worker'),
    ]

    operations = [
        migrations.CreateModel(
            name='Day_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=200)),
                ('Lunch_A', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(max_length=200)),
                ('lecture', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
