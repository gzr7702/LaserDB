# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
            name='Charge',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('purchase_order', models.IntegerField()),
                ('zone', models.IntegerField()),
                ('parts', models.IntegerField()),
                ('total', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
                ('billing_address', models.ForeignKey(to='repairs.Address', related_name='address_billing')),
                ('street_address', models.ForeignKey(to='repairs.Address', related_name='address_street')),
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
                ('software_version', models.CharField(max_length=200)),
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
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceEngineer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
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
                ('payment_category', models.CharField(max_length=20, choices=[('installation', 'Installation'), ('billable_repair', 'Billable Repair'), ('sales_mkt_dem', 'Sales/Mkt/Dem'), ('contract_repair', 'Contract Repair'), ('warranty_repair', 'Warranty Repair')])),
                ('service_category', models.CharField(max_length=20, choices=[('service', 'Service'), ('complaint', 'Complaint'), ('medical_device_report', 'Medical Device Report')])),
                ('charges', models.OneToOneField(to='repairs.Charge')),
                ('customer', models.ForeignKey(to='repairs.Customer')),
                ('engineer', models.OneToOneField(to='repairs.ServiceEngineer')),
                ('machine', models.ForeignKey(to='repairs.Machine')),
                ('parts', models.ManyToManyField(to='repairs.Part')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
