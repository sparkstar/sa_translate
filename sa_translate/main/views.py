# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader

from models import Entries

def mainpage(request):
    entries = Entries.objects.all().order_by('-Writedate')[0:1]
    tpl = loader.get_template('main/main.html')
    ctx = RequestContext(request, {'entries':entries})
    return HttpResponse(tpl.render(ctx))


