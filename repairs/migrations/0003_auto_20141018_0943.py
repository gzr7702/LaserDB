# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0002_auto_20141018_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='software_version',
            field=models.FloatField(),
        ),
    ]
