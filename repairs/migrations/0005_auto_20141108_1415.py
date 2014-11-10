# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repairs', '0004_auto_20141108_0151'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='name',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='address',
            name='contact_name',
        ),
        migrations.AddField(
            model_name='customer',
            name='contact_name',
            field=models.CharField(blank=True, max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servicelog',
            name='parts',
            field=models.OneToOneField(to='repairs.Part', blank=True, null=True),
        ),
    ]
