from django.forms import forms
import repairs.models

class TechForm(forms.Form):
    class Meta:
        model = Technician

class MachineForm(forms.Form):
    class Meta:
        model = Machine

class CustomerForm(forms.Form):
    class Meta:
        model = Customer