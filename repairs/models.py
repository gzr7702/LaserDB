from django.db import models
from django.db.models.fields import IntegerField, CharField, TextField
import pprint

class Machine(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    model = CharField(max_length=200)
    manufacture_date = models.DateField()
    software_version = models.FloatField()
    passwd = models.CharField(max_length=200)
    pulse_count = models.IntegerField()
    
    def __str__(self):
        items = [str(self.serial_number), self.model, str(self.manufacture_date),\
                 str(self.software_version), self.passwd, str(self.pulse_count)]
        item_string = '\t'.join(items)
        return item_string
    
class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip = models.IntegerField()
    phone = models.CharField(max_length=12)
    contact_name = models.CharField(max_length=200)
    
    def __str__(self):
        items = [self.contact_name, self.street, self.city, self.state, \
                 str(self.zip), self.phone]
        item_string = '\t'.join(items)
        return item_string

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    street_address = models.ForeignKey(Address, related_name='address_street')
    billing_address = models.ForeignKey(Address, related_name='address_billing')

    def __str__(self):
        items = [self.name, self.email]
        item_string = '\t'.join(items)
        return item_string
    
class ServiceEngineer(models.Model):
    first_name = CharField(max_length=200)
    last_name = CharField(max_length=200)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Part(models.Model):
    serial_number = models.IntegerField(primary_key=True)
    part_number = models.IntegerField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self):
        items = [str(self.serial_number), str(self.part_number), str(self.price), str(self.quantity)]
        item_string = '\t'.join(items)
        return item_string
    
class Charge(models.Model):
    purchase_order = models.IntegerField()
    zone_charge = models.DecimalField(max_digits=9, decimal_places=2)
    parts_charge = models.DecimalField(max_digits=9, decimal_places=2)
    #take total out of admin since it's not a real total?
    total_charge = models.DecimalField(null=True, blank=True, max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.purchase_order)
    
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
    
    #this should be in the form model, no?================================
    
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

    def __str__(self):
        return str(self.rma_number)
