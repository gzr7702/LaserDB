from django.forms import ModelForm, ModelMultipleChoiceField
from service_orders.models import ServiceLog, ServiceEngineer, Machine, Customer, Address, Part
from django.forms.widgets import DateInput, Select 
from django.forms.models import modelformset_factory

class EngineerForm(ModelForm):
    class Meta:
        model = ServiceEngineer

class CustomerForm(ModelForm):
    #customer, addresses
    class Meta:
        model = Customer

class AddressForm(ModelForm):
    class Meta:
        model = Address

class MachineForm(ModelForm):
    #machine
    class Meta:
        model = Machine
        widgets = {
                   'manufacture_date': DateInput(attrs={'type':'date'}),
                   }
        
class PartsForm(ModelForm):
    class Meta:
        model = Part

class ServiceForm(ModelForm):
    #correction, notes, charges, payment category, service category, condition
    class Meta:
        model = ServiceLog
        #fields = ['correction', 'notes', 'purchase_order',\
        #          'zone_charge', 'parts_charge', 'payment_category',\
        #          'service_category', 'condition']