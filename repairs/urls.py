from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'repairs.views.repair_home', name='repair_home'),
    url(r'repair_form$', 'repairs.views.repair_form', name='repair_form'),
)