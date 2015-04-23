from django.conf.urls import patterns, include, url
from django.contrib import admin
from service_orders.form_views import ServiceOrderWizard, WIZARD_FORMS

urlpatterns = patterns('',
    url(r'^$', 'service_orders.views.home', name='service_order_home'),
    url(r'individualreport/(?P<rma_number>\d+)/$', 'service_orders.views.individual_report', name='individual_report'),
    url(r'engineerform/$', 'service_orders.form_views.engineer_form', name='engineer_form'),
    url(r'customerform/$', 'service_orders.form_views.customer_form', name='customer_form'),
    url(r'addressform/$', 'service_orders.form_views.address_form', name='address_form'),
    url(r'machineform/$', 'service_orders.form_views.machine_form', name='machine_form'),
    url(r'partsform/$', 'service_orders.form_views.parts_form', name='parts_form'),
    #url(r'addpart/$', 'service_orders.form_views.add_parts_form', name='add_parts_form'),
    url(r'^serviceform/$', ServiceOrderWizard.as_view(WIZARD_FORMS)),
)