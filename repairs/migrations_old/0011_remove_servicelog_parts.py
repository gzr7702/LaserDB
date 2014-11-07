# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0010_auto_20141103_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicelog',
            name='parts',
        ),
    ]
