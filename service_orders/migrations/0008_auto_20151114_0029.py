# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0007_auto_20151029_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=200),
        ),
    ]
