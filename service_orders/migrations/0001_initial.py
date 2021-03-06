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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.IntegerField()),
                ('phone', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=200)),
                ('contact_name', models.CharField(null=True, max_length=200, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('billing_address', models.ForeignKey(to='service_orders.Address', related_name='address_billing')),
                ('street_address', models.ForeignKey(to='service_orders.Address', related_name='address_street')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('serial_number', models.IntegerField(serialize=False, primary_key=True)),
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
                ('serial_number', models.IntegerField(serialize=False, primary_key=True)),
                ('part_number', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('location', models.CharField(max_length=200)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceEngineer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('rma_number', models.IntegerField(serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('condition', models.TextField(max_length=500)),
                ('correction', models.TextField(max_length=500)),
                ('notes', models.TextField(max_length=500)),
                ('purchase_order', models.IntegerField(default=0)),
                ('zone_charge', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=9)),
                ('parts_charge', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=9)),
                ('total_charge', models.DecimalField(null=True, decimal_places=2, default=Decimal('0.0000'), blank=True, max_digits=9)),
                ('payment_category', models.CharField(max_length=20, choices=[('installation', 'Installation'), ('billable_repair', 'Billable Repair'), ('sales_mkt_dem', 'Sales/Mkt/Dem'), ('contract_repair', 'Contract Repair'), ('warranty_repair', 'Warranty Repair')])),
                ('service_category', models.CharField(max_length=22, choices=[('service', 'Service'), ('complaint', 'Complaint'), ('medical_device_report', 'Medical Device Report')])),
                ('customer', models.ForeignKey(to='service_orders.Customer')),
                ('engineer', models.ForeignKey(to='service_orders.ServiceEngineer')),
                ('machine', models.ForeignKey(to='service_orders.Machine')),
                ('parts', models.OneToOneField(to='service_orders.Part')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
