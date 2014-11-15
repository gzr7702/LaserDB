from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'parts_inventory.views.parts_home', name='parts_home'),
    url(r'report/(?P<serial_number>\d+)/$', 'parts.views.parts_report', name='parts_report'),
)