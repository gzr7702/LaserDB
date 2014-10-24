from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'LaserDB.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^repairs/', include('repairs.urls')),
    url(r'^parts/', include('parts.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
