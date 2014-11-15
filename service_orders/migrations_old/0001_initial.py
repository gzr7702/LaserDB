# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.IntegerField()),
                ('phone', models.CharField(max_length=12)),
                ('contact_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('billing_address', models.ForeignKey(related_name='address_billing', to='repairs.Address')),
                ('street_address', models.ForeignKey(related_name='address_street', to='repairs.Address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('manufacture_date', models.DateField()),
                ('software_version', models.FloatField()),
                ('passwd', models.CharField(max_length=200)),
                ('pulse_count', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('serial_number', models.IntegerField(primary_key=True, serialize=False)),
                ('part_number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceEngineer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceLog',
            fields=[
                ('rma_number', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('condition', models.TextField(max_length=500)),
                ('correction', models.TextField(max_length=500)),
                ('notes', models.TextField(max_length=500)),
                ('purchase_order', models.IntegerField(default=0)),
                ('zone_charge', models.DecimalField(max_digits=9, default=Decimal('0.0000'), decimal_places=2)),
                ('parts_charge', models.DecimalField(max_digits=9, default=Decimal('0.0000'), decimal_places=2)),
                ('total_charge', models.DecimalField(null=True, decimal_places=2, max_digits=9, default=Decimal('0.0000'), blank=True)),
                ('payment_category', models.CharField(choices=[('installation', 'Installation'), ('billable_repair', 'Billable Repair'), ('sales_mkt_dem', 'Sales/Mkt/Dem'), ('contract_repair', 'Contract Repair'), ('warranty_repair', 'Warranty Repair')], max_length=20)),
                ('service_category', models.CharField(choices=[('service', 'Service'), ('complaint', 'Complaint'), ('medical_device_report', 'Medical Device Report')], max_length=20)),
                ('customer', models.ForeignKey(to='repairs.Customer')),
                ('engineer', models.ForeignKey(to='repairs.ServiceEngineer')),
                ('machine', models.ForeignKey(to='repairs.Machine')),
                ('parts', models.OneToOneField(null=True, to='repairs.Part')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
