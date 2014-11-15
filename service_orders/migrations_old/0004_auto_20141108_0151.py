# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0003_auto_20141108_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Part',
            fields=[
                ('serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('part_number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='servicelog',
            name='part_number',
        ),
        migrations.RemoveField(
            model_name='servicelog',
            name='part_price',
        ),
        migrations.RemoveField(
            model_name='servicelog',
            name='part_quantity',
        ),
        migrations.RemoveField(
            model_name='servicelog',
            name='part_serial_number',
        ),
        migrations.AddField(
            model_name='servicelog',
            name='parts',
            field=models.OneToOneField(null=True, to='repairs.Part'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='manufacture_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='machine',
            name='passwd',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='machine',
            name='software_version',
            field=models.FloatField(),
        ),
    ]
