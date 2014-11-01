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

class MachineForm(ModelForm):
    #machine
    class Meta:
        model = Machine

class AssessmentForm(ModelForm):
    #correction, notes, parts, charges, payment category, service category, condition
    class Meta:
        model = ServiceLog
        fields = ['correction', 'notes', 'parts', 'charges', 'payment_category',\
                  'service_category', 'condition']