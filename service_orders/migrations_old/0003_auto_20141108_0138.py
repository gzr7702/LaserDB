# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0002_auto_20141107_0241'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicelog',
            name='parts',
        ),
        migrations.DeleteModel(
            name='Part',
        ),
        migrations.AddField(
            model_name='servicelog',
            name='part_number',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicelog',
            name='part_price',
            field=models.DecimalField(blank=True, max_digits=9, null=True, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicelog',
            name='part_quantity',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicelog',
            name='part_serial_number',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='machine',
            name='manufacture_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='passwd',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='machine',
            name='software_version',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
