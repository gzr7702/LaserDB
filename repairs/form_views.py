
from django.contrib.formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response
from .forms import InfoForm, CustomerForm, MachineForm, AssessmentForm

FORMS = [("info", InfoForm),
         ("customer", CustomerForm),
         ("machine", MachineForm),
         ("assessment", AssessmentForm)]

TEMPLATES = {"info": "infoform.html",
             "customer": "customerform.html",
             "machine": "machineform.html",
             "assessment": "assessmentform.html"}

class ServiceOrderWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        #probably don't need to pass form_data to template
        return render_to_response('done.html')
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    #write to db here
    
    return form_data