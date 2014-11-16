
from django.contrib.formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response
from .forms import EngineerForm, CustomerForm, AddressForm, MachineForm, PartsForm, ServiceForm
from django.forms.models import ModelForm
from django.template.context import RequestContext
from cherrypy._cperror import HTTPRedirect
from django.http.response import HttpResponseRedirect

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

def engineer_form(request):
    form = EngineerForm(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
        return HttpResponseRedirect('')
    return render_to_response('engineerform.html', locals(), context_instance=RequestContext(request))

def customer_form(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
        return HttpResponseRedirect('')
    return render_to_response('customerform.html', locals(), context_instance=RequestContext(request))

def address_form(request):
    form = AddressForm(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
        return HttpResponseRedirect('')
    return render_to_response('addressform.html', locals(), context_instance=RequestContext(request))

def machine_form(request):
    form = MachineForm(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
        return HttpResponseRedirect('')
    return render_to_response('machineform.html', locals(), context_instance=RequestContext(request))

def parts_form(request):
    form = PartsForm(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
        return HttpResponseRedirect('')
    return render_to_response('partsform.html', locals(), context_instance=RequestContext(request))

class ServiceOrderWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        process_form_data(form_list)
        return render_to_response('done.html')
    
def process_form_data(form_list):
    form_data = [form.cleaned_data for form in form_list]
    print(form_data)
    #write to db here
    
    return form_data