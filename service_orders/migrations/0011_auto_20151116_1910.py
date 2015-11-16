# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0010_auto_20151114_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelog',
            name='notes',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
