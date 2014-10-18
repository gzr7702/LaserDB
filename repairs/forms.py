from django.forms import forms
from repairs.models import ServiceEngineer, Machine, Customer

class SerciceEngineerForm(forms.Form):
    class Meta:
        model = ServiceEngineer 

class MachineForm(forms.Form):
    class Meta:
        model = Machine

class CustomerForm(forms.Form):
    class Meta:
        model = Customer