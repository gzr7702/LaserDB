# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parts_inventory', '0002_part_used'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='part',
            name='quantity',
        ),
    ]
