# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0003_auto_20151017_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='billing_address',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='street_address',
        ),
        migrations.AddField(
            model_name='address',
            name='address_type',
            field=models.CharField(default='street', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(null=True, related_name='customer', to='service_orders.Customer'),
            preserve_default=True,
        ),
    ]
