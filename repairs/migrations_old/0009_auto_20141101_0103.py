# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0008_auto_20141101_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicelog',
            name='charges',
        ),
        migrations.DeleteModel(
            name='Charge',
        ),
        migrations.AddField(
            model_name='servicelog',
            name='parts_charge',
            field=models.DecimalField(default=Decimal('0.0000'), decimal_places=2, max_digits=9),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicelog',
            name='purchase_order',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicelog',
            name='total_charge',
            field=models.DecimalField(max_digits=9, default=Decimal('0.0000'), decimal_places=2, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='servicelog',
            name='zone_charge',
            field=models.DecimalField(default=Decimal('0.0000'), decimal_places=2, max_digits=9),
            preserve_default=True,
        ),
    ]
