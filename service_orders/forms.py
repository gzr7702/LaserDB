from django.forms import ModelForm, ModelMultipleChoiceField
from service_orders.models import ServiceLog, ServiceEngineer, Machine, Customer, Address, Part
from django.forms.widgets import DateInput, Select, TextInput
from django.forms.models import modelformset_factory

class EngineerForm(ModelForm):
    class Meta:
        model = ServiceEngineer
        fields = "__all__"

class CustomerForm(ModelForm):
    #customer, addresses
    class Meta:
        model = Customer
        fields = "__all__"

class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = "__all__"

class MachineForm(ModelForm):
    #machine
    class Meta:
        model = Machine
        fields = "__all__"
        widgets = {
                   'manufacture_date': DateInput(attrs={'type':'date'}),
                   }
        
class PartsForm(ModelForm):
    class Meta:
        model = Part
        fields = "__all__"

class InfoForm(ModelForm):
    class Meta:
        model = ServiceLog
        fields = ['engineer', 'rma_number', 'date', 'customer', 'machine', 'condition']
        widgets = { 'date': DateInput(attrs={'type':'date'}),}

class AssessmentForm(ModelForm):
    class Meta:
        model = ServiceLog
        fields = ['correction', 'notes']

class InvoiceForm(ModelForm):
    class Meta:
        #how do we pass the parts model in here?
        model = ServiceLog
        available_parts = Part.objects.filter(used=False)
        fields = ['purchase_order', 'zone_charge', 'parts_charge',\
                  'payment_category', 'service_category']

class ConfirmationForm(ModelForm):
    class Meta:
        model = ServiceLog
        fields = "__all__"