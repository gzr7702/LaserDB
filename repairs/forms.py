from django.forms import ModelForm
from repairs.models import ServiceLog, ServiceEngineer, Machine, Customer, Address, Part

class EngineerForm(ModelForm):
    class Meta:
        model = ServiceEngineer

class InfoForm(ModelForm):
    #rma, date
    class Meta:
        model = ServiceLog
        fields = ['rma_number', 'date']

class CustomerForm(ModelForm):
    #customer, addresses
    class Meta:
        model = Customer
        fields = ['company_name', 'contact_name', 'email']

class AddressForm(ModelForm):
    class Meta:
        model = Address

class MachineForm(ModelForm):
    #machine
    class Meta:
        model = Machine
        fields = ['serial_number', 'model', 'manufacture_date', 'software_version', 'passwd', 'pulse_count']
        
class PartsForm(ModelForm):
    class Meta:
        model = Part

class AssessmentForm(ModelForm):
    #correction, notes, charges, payment category, service category, condition
    class Meta:
        model = ServiceLog
        fields = ['correction', 'notes', 'purchase_order',\
                  'zone_charge', 'parts_charge', 'payment_category',\
                  'service_category', 'condition']