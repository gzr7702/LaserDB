from django.conf.urls import patterns, include, url
from django.contrib import admin
from repairs.forms import InfoForm, CustomerForm, MachineForm, AssessmentForm
from repairs.form_views import ServiceOrderWizard, FORMS

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'repairs.views.repair_home', name='repair_home'),
    #url(r'repair-form/$', 'repairs.views.repair_form', name='repair_form'),
    url(r'individual-report/(?P<rma_number>\d+)/$', 'repairs.views.individual_report', name='individual_report'),
    url(r'^repair-form/$', ServiceOrderWizard.as_view(FORMS)),
)