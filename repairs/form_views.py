
from django.contrib.formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response

class ServiceOrderWizard(SessionWizardView):
    template_name = 'service_form.html'

    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)
        print("form data", form_data)
        #probably don't need to pass form_data to template
        return render_to_response('done.html', {'form_data':form_data})
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    #write to db here
    
    return form_data