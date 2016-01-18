# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idTAG')),
                ('diversion', models.FloatField(null=True, verbose_name=b'Diversion', db_column=b'DEVIATION', blank=True)),
                ('max_time', models.IntegerField(null=True, verbose_name=b'Max time', db_column=b'TIME_MAX', blank=True)),
                ('conv_rate', models.IntegerField(null=True, verbose_name=b'Convertion rate', db_column=b'CONV_RATE', blank=True)),
            ],
            options={
                'db_table': 'tag',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagInfo',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idTAGINFO')),
                ('name', models.CharField(max_length=45, verbose_name=b'Name', db_column=b'NAME')),
                ('description', models.CharField(max_length=255, verbose_name=b'Details', db_column=b'DESCRIPTION', blank=True)),
            ],
            options={
                'db_table': 'taginfo',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
