# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0007_auto_20141118_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelog',
            name='parts',
            field=models.OneToOneField(to='service_orders.Part'),
        ),
    ]
