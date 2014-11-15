# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_orders', '0005_auto_20141108_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicelog',
            name='service_category',
            field=models.CharField(choices=[('service', 'Service'), ('complaint', 'Complaint'), ('medical_device_report', 'Medical Device Report')], max_length=22),
        ),
    ]
