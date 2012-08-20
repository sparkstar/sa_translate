# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

from sa_translate.main.views import *
from sa_translate.viewjp.views import *

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

    url(r'^$', 'sa_translate.main.views.mainpage'),
    url(r'^surgingaura/$', 'sa_translate.viewjp.views.mainview'),
    
    url(r'^surgingaura/viewtext/translatepost/$', 'sa_translate.viewjp.views.translatePost'),
    url(r'^surgingaura/viewtext/choosetext/$', 'sa_translate.viewjp.views.chooseTranslated'),
    url(r'^surgingaura/viewtext/unchoosetext/$', 'sa_translate.viewjp.views.unchooseTranslated'),   
    url(r'^surgingaura/viewtext/deltranslatetext/$', 'sa_translate.viewjp.views.delTranslated'),     
    url(r'^surgingaura/viewtext/(?P<number>\d+)/$', 'sa_translate.viewjp.views.viewText'),

    url(r'^surgingaura/listview/$', 'sa_translate.viewjp.views.viewList'),
    url(r'^surgingaura/listview/(?P<page>\d+)/$', 'sa_translate.viewjp.views.viewList'), 

    url(r'^surgingaura/alllist/$', 'sa_translate.viewjp.views.allList'),

    
    url(r'^surgingaura/downloadfull/$', 'sa_translate.viewjp.views.downloadFullIps'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': ROOT_PATH+'/media'}),


    url(r'^admin/', include(admin.site.urls)),
)
