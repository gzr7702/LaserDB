# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0008_auto_20151114_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='service_log',
            field=models.ForeignKey(null=True, to='service_orders.ServiceLog', blank=True),
        ),
    ]
