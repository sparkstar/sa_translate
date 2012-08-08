from django.conf.urls.defaults import patterns, include, url

from main.views import *
from viewjp.views import *

import os
ROOT_PATH = os.path.dirname(__file__)

from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sa_translate.views.home', name='home'),
    # url(r'^sa_translate/', include('sa_translate.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'main.views.mainpage'),
    url(r'^viewtext/(?P<number>\d+)/$', 'viewjp.views.viewText'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': ROOT_PATH+'/media'}),


    url(r'^admin/', include(admin.site.urls)),
)