# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0013_auto_20141104_0302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('part_number', models.IntegerField()),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='servicelog',
            name='parts',
            field=models.OneToOneField(to='repairs.Part', null=True),
            preserve_default=True,
        ),
    ]
