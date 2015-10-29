# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0006_auto_20151018_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='software_version',
            field=models.CharField(max_length=200),
        ),
    ]
