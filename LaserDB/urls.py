from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'LaserDB.views.home', name='home'),
    url(r'^serviceorders/', include('service_orders.urls')),
    url(r'^partsinventory/', include('service_orders.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
    
    #user auth urls
    url(r'^accounts/login/$', 'LaserDB.views.login', name='login'),
    url(r'^accounts/auth/$', 'LaserDB.views.auth_view', name='auth'),
    url(r'^accounts/logout/$', 'LaserDB.views.logout_view', name='logout'),
    url(r'^accounts/loggedin/$', 'LaserDB.views.loggedin', name='loggedin'),
    url(r'^accounts/invalid/$', 'LaserDB.views.invalid_login', name='invalid_login'),
    
)
