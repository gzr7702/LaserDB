# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0006_auto_20141018_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charge',
            name='total_charge',
            field=models.DecimalField(null=True, decimal_places=2, blank=True, max_digits=9),
        ),
    ]
