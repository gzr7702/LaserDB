# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0004_auto_20141018_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charge',
            name='parts',
        ),
        migrations.RemoveField(
            model_name='charge',
            name='total',
        ),
        migrations.RemoveField(
            model_name='charge',
            name='zone',
        ),
        migrations.AddField(
            model_name='charge',
            name='parts_charge',
            field=models.DecimalField(default=8.0, decimal_places=2, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charge',
            name='total_charge',
            field=models.DecimalField(default=8.0, decimal_places=2, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='charge',
            name='zone_charge',
            field=models.DecimalField(default=9.0, decimal_places=2, max_digits=9),
            preserve_default=False,
        ),
    ]
