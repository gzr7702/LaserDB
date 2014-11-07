# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0007_auto_20141018_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelog',
            name='engineer',
            field=models.ForeignKey(to='repairs.ServiceEngineer'),
        ),
    ]
