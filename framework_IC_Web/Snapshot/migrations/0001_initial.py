# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idSNAP')),
                ('value', models.FloatField(verbose_name=b'Value', db_column=b'VALUE')),
                ('snapshot', models.DateTimeField(verbose_name=b'Snapshot', db_column=b'SNAPSHOT')),
            ],
            options={
                'db_table': 'snapshot',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
