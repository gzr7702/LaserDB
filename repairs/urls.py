from django.conf.urls import patterns, include, url
from django.contrib import admin
from repairs.forms import EngineerForm, CustomerForm, MachineForm, AddressForm, PartsForm, ServiceForm
from repairs.form_views import ServiceOrderWizard 

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'repairs.views.repair_home', name='repair_home'),
    #url(r'repair-form/$', 'repairs.views.repair_form', name='repair_form'),
    url(r'individualreports/(?P<rma_number>\d+)/$', 'repairs.views.individual_report', name='individual_report'),
    url(r'engineerform/$', 'repairs.form_views.engineer_form', name='engineer_form'),
    #url(r'^serviceform/$', ServiceOrderWizard.as_view(ServiceForm)),
)