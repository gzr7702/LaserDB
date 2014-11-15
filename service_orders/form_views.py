
from django.contrib.formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response
from .forms import EngineerForm, CustomerForm, AddressForm, MachineForm, PartsForm, ServiceForm
from django.forms.models import ModelForm

"""FORMS = [("engineer", EngineerForm),
         ("info", InfoForm),
         ("customer", CustomerForm),
         ("address", AddressForm),
         ("machine", MachineForm),
         ("part", PartsForm),
         ("assessment", AssessmentForm)]
         """

TEMPLATES = {"engineer": "engineerform.html",
             "machine": "machineform.html",
             "customer": "customerform.html",
             "address": "addressform.html",
             "part": "partform.html",
             "service": "serviceform.html"}

def engineer(ModelForm):
    pass

class ServiceOrderWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        process_form_data(form_list)
        #probably don't need to pass form_data to template
        return render_to_response('done.html')
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    print(form_data)
    #write to db here
    
    return form_data