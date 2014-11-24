# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0008_auto_20141120_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelog',
            name='parts',
            field=models.OneToOneField(null=True, blank=True, to='service_orders.Part'),
        ),
    ]
