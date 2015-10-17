from django.db import models
from django.db.models.fields import IntegerField, CharField, TextField
import pprint
from decimal import Decimal

class Machine(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    model = CharField(max_length=200)
    manufacture_date = models.DateField()
    software_version = models.FloatField()
    passwd = models.CharField(max_length=200)
    pulse_count = models.IntegerField()
    
    def __str__(self):
        return self.model + " " + str(self.serial_number)

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()
    phone = models.CharField(max_length=12)
    
    def __str__(self):
        items = [self.street, self.city, self.state, \
                 str(self.zip), self.phone]
        item_string = '\t'.join(items)
        return item_string

class Customer(models.Model):
    company_name = models.CharField(max_length=200)
    contact_name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    street_address = models.ForeignKey(Address, related_name='address_street')
    billing_address = models.ForeignKey(Address, related_name='address_billing')

    def __str__(self):
        return self.company_name
    
class ServiceEngineer(models.Model):
    first_name = CharField(max_length=200)
    last_name = CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Part(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    part_number = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    location = models.CharField(max_length=200)
    used = models.BooleanField(default=False)

    def __str__(self):
        items = [str(self.serial_number), str(self.part_number),\
                str(self.price), self.location]
        item_string = '\t'.join(items)
        return item_string
    
class ServiceLog(models.Model):
    rma_number = models.IntegerField(primary_key=True)
    date = models.DateField()
    customer = models.ForeignKey(Customer)
    machine = models.ForeignKey(Machine)
    condition = models.TextField(max_length=500) #condition/cause
    correction = models.TextField(max_length=500)
    notes = models.TextField(max_length=500)
    #make this one to many?
    parts = models.ForeignKey(Part)
    engineer = models.ForeignKey(ServiceEngineer)
    purchase_order = models.IntegerField(default=0)
    zone_charge = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
    parts_charge = models.DecimalField(max_digits=9, decimal_places=2, default=Decimal('0.00'))
    #take total out of admin since it's not a real total and compute on input?
    total_charge = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=2, default=Decimal('0.0000'))
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
    service_category = models.CharField(max_length=22,
                                choices=SERVICE_CATEGORY_CHOICES)

    def __str__(self):
        return str(self.rma_number)
