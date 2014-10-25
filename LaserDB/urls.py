from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'LaserDB.views.home', name='home'),
    url(r'^repairs/', include('repairs.urls')),
    url(r'^parts/', include('parts.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    #user auth urls
    url(r'^accounts/login/$', 'LaserDB.views.login'),
    url(r'^accounts/auth/$', 'LaserDB.views.auth_view'),
    url(r'^accounts/logout/$', 'LaserDB.views.logout'),
    url(r'^accounts/loggedin/$', 'LaserDB.views.loggedin'),
    url(r'^accounts/invalid/$', 'LaserDB.views.invalid_login'),
    
)
