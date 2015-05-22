# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Day_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=200, editable=False)),
                ('breakfast', models.CharField(default=b'with', max_length=200)),
                ('Lunch_A', models.CharField(max_length=200)),
                ('Lunch_B', models.CharField(max_length=200)),
                ('lecture', models.CharField(default=b'none', max_length=200)),
                ('order', models.IntegerField(default=b'0', editable=False)),
                ('dinner', models.CharField(default=b'with', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_Name', models.CharField(max_length=200)),
                ('last_Name', models.CharField(max_length=200)),
                ('arrival_Date', models.DateField(null=True, blank=True)),
                ('departure_Date', models.DateField(null=True, blank=True)),
                ('contact_info', models.CharField(max_length=200, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_Name', models.CharField(max_length=200)),
                ('crew_Size', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200, null=True, blank=True)),
                ('days', models.ManyToManyField(to='workCrew.Day_Info', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_Name', models.CharField(max_length=200)),
                ('last_Name', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=200, null=True, blank=True)),
                ('arrival_Date', models.DateField(null=True, blank=True)),
                ('departure_Date', models.DateField(null=True, blank=True)),
                ('active', models.NullBooleanField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
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
        migrations.CreateModel(
            name='WorkNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='work_Note',
            field=models.ForeignKey(blank=True, to='workCrew.WorkNote', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='helper',
            name='jobs',
            field=models.ManyToManyField(to='workCrew.Job'),
            preserve_default=True,
        ),
    ]
