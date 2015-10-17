# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0002_auto_20151014_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicelog',
            name='parts',
        ),
        migrations.AddField(
            model_name='part',
            name='service_log',
            field=models.ForeignKey(to='service_orders.ServiceLog', null=True),
            preserve_default=True,
        ),
    ]
