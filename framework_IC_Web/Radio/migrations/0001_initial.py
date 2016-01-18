# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radio',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idRADIO')),
                ('endreal', models.CharField(max_length=64, verbose_name=b'Full address', db_column=b'ENDREAL', blank=True)),
            ],
            options={
                'db_table': 'radio',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RadioInfo',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idRADIOINFO')),
                ('name', models.CharField(max_length=45, verbose_name=b'Name', db_column=b'NAME')),
                ('description', models.CharField(max_length=300, verbose_name=b'Details', db_column=b'DESCRIPTION', blank=True)),
            ],
            options={
                'db_table': 'radioinfo',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
