from django.db import models
from django.db.models.fields import IntegerField, CharField, TextField
from Crypto.Random.random import choice

class Machine(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    model = CharField(max_length=200)
    manufacture_date = models.DateField()
    software_version = models.CharField(max_length=200)
    passwd = models.CharField(max_length=200)
    pulse_count = models.IntegerField()
    
class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()
    phone = models.CharField(max_length=12)
    contact_name = models.CharField(max_length=200)

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    street_address = models.ManyToOneRel(Address)
    billing_address = models.ManyToOneRel(Address)
    
class ServiceEngineer(models.Model):
    first_name = CharField(max_length=200)
    last_name = CharField(max_length=200)
    
class Part(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    part_number = models.IntegerField()
    price = models.IntegerField()
    quantity = models.IntegerField()

class Charge(models.Model):
    purchase_order = models.IntegerField()
    zone = models.IntegerField()
    parts = models.IntegerField()
    total = models.IntegerField()
    
class ServiceLog(models.Model):
    rma_number = models.IntegerField(primary_key=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer)
    machine = models.ForeignKey(Machine)
    condition = models.TextField(max_length=500) #condition/cause
    correction = models.TextField(max_length=500)
    notes = models.TextField(max_length=500)
    parts = models.ManyToManyField(Part)
    engineer = models.OneToOneField(ServiceEngineer)
    charges = models.OneToOneField(Charge)
    
    PAYMENT_CATEGORY_CHOICES = (
                                ('installation', 'Installation'), 
                                ('billable_repair', 'Billable Repair'), 
                                ('sales_mkt_dem', 'Sales/Mkt/Dem'), 
                                ('contract_repair', 'Contract Repair'), 
                                ('warranty_repair', 'Warranty Repair')
                                )
    payment_category = models.CharField(max_length=20,
                                        choices=PAYMENT_CATEGORY_CHOICES)

    #in controller add: service catagories,
    #text field is filled out if the last 2 are checked.
    SERVICE_CATEGORY_CHOICES = (
                                ('service', 'Service'), 
                                ('complaint', 'Complaint'), 
                                ('medical_device_report', 'Medical Device Report')
                                )
    service_category = models.CharField(max_length=20,
                                choices=SERVICE_CATEGORY_CHOICES)
