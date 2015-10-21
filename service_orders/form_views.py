
from django.contrib.formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response
from .forms import EngineerForm, CustomerForm, AddressForm, MachineForm, PartsForm, InfoForm, AssessmentForm, InvoiceForm, ConfirmationForm
from .models import ServiceLog
from django.forms.models import ModelForm
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect

WIZARD_FORMS = [("info", InfoForm),
         ("assessment", AssessmentForm),
         ("invoice", InvoiceForm),]
         #("confirmation", ConfirmationForm)]

TEMPLATES = {"info": "infoform.html",
             "assessment": "assessmentform.html",
             "invoice": "invoiceform.html"}
             #"confirmation": "confirmationform.html"}

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

def add_parts_form(request):
    """Add parts from the Service Order page"""
    form = PartsForm(request.POST or None)
    if form.is_valid():
        save_form = form.save(commit=False)
        save_form.save()
        return HttpResponseRedirect('')
    return render_to_response('addpart.html', locals(), context_instance=RequestContext(request))

def process_form_data(form_list):
    instance = ServiceLog()
    for form in form_list:
        for field, value in form.cleaned_data.items():
            setattr(instance, field, value)
    # Total zone_charge and parts_charge and set attribute
    total = instance.parts_charge + instance.zone_charge
    setattr(instance, total_charge, total)
    instance.save()

class ServiceOrderWizard(SessionWizardView):
    def get_template_names(self):
        #import pdb; pdb.set_trace()
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        print("in done ---------------------")
        process_form_data(form_list)
        #return HttpResponseRedirect('done.html')
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
    