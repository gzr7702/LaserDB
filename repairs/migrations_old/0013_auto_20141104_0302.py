# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0012_servicelog_parts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicelog',
            name='parts',
        ),
        migrations.DeleteModel(
            name='Part',
        ),
    ]
