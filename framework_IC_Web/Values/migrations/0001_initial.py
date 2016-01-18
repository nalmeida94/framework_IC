# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Values',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idVALUES')),
                ('value', models.FloatField(verbose_name=b'Value', db_column=b'VALUE')),
                ('datetime', models.DateTimeField(verbose_name=b'Date time', db_column=b'DATETIME')),
            ],
            options={
                'db_table': 'values',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
