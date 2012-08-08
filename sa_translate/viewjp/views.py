# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from models import Text
import re

def viewText(request, number):
    entries = Text.objects.get(textNumber = number)
    
    parsedText = re.findall('..', entries.hexString)
    
    temptext = []
    text = []
    
    z = 0
    while z < len(parsedText):
        if re.match('f.', parsedText[z]):
            text.append(parsedText[z] + parsedText[z + 1])
            z = z + 1
        else:
            text.append(parsedText[z])
            
        z = z + 1
 

    tpl = loader.get_template('viewjp/viewjp.html')
    ctx = RequestContext(request, {'text':text})
    return HttpResponse(tpl.render(ctx))


    