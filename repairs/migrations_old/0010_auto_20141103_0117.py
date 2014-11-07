# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0009_auto_20141101_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelog',
            name='parts',
            field=models.OneToOneField(to='repairs.Part'),
        ),
    ]
