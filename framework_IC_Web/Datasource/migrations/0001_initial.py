# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Datasource',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idDATASOURCE')),
                ('name', models.CharField(max_length=45, verbose_name=b'Name', db_column=b'NAME')),
                ('manufacturer', models.CharField(max_length=45, verbose_name=b'Manufacturer', db_column=b'MANUFACTURER', blank=True)),
                ('model', models.CharField(max_length=45, verbose_name=b'Model', db_column=b'MODEL', blank=True)),
            ],
            options={
                'db_table': 'datasource',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
