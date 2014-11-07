# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0011_remove_servicelog_parts'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicelog',
            name='parts',
            field=models.ManyToManyField(to='repairs.Part'),
            preserve_default=True,
        ),
    ]
