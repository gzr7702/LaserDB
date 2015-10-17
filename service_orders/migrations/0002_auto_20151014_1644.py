# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelog',
            name='parts',
            field=models.ForeignKey(to='service_orders.Part'),
        ),
    ]
