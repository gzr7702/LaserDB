# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0003_auto_20141018_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='part',
            name='price',
            field=models.DecimalField(max_digits=9, decimal_places=2),
        ),
    ]
