from django.forms import ModelForm
from repairs.models import ServiceLog, ServiceEngineer, Machine, Customer

class InfoForm(ModelForm):
    #rma, date, engineer
    class Meta:
        model = ServiceLog
        fields = ['rma_number', 'date', 'engineer']

class CustomerForm(ModelForm):
    #customer, addresses
    class Meta:
        model = Customer
        fields = ['name', 'email', 'street_address', 'billing_address']

class MachineForm(ModelForm):
    #machine
    class Meta:
        model = Machine
        fields = ['serial_number', 'model', 'manufacture_date', 'software_version', 'passwd', 'pulse_count']

class AssessmentForm(ModelForm):
    #correction, notes, parts, charges, payment category, service category, condition
    class Meta:
        model = ServiceLog
        fields = ['correction', 'notes', 'parts', 'purchase_order',\
                  'zone_charge', 'parts_charge', 'payment_category',\
                  'service_category', 'condition']