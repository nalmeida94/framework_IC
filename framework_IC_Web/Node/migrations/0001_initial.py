# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.IntegerField(verbose_name=b'Id', serialize=False, editable=False, primary_key=True, db_column=b'idSITE')),
                ('name', models.CharField(max_length=45, verbose_name=b'Name', db_column=b'NAME')),
                ('information', models.CharField(max_length=45, verbose_name=b'Details', db_column=b'INFORMATION', blank=True)),
            ],
            options={
                'db_table': 'site',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
