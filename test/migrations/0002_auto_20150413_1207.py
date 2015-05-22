# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workCrew', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Helper',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstName', models.CharField(max_length=200)),
                ('lastName', models.CharField(max_length=200)),
                ('contact_info', models.CharField(max_length=200)),
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
        migrations.AlterField(
            model_name='student',
            name='workNote',
            field=models.ForeignKey(to='workCrew.WorkNote'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='work',
            name='helperName',
            field=models.ForeignKey(to='workCrew.Helper'),
            preserve_default=True,
        ),
    ]
