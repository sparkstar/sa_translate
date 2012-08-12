# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext, loader

from models import Text
import re

def viewText(request, number):
    entries = Text.objects.get(textNumber = number)
    
    parsedText = re.findall('f...|..', entries.hexString)
    '''
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
 
    '''
    
    text = jpcapProcess(parsedText)
    
    tpl = loader.get_template('viewjp/viewjp.html')
#    ctx = RequestContext(request, {'text':text})
    ctx = RequestContext(request, {})
    return HttpResponse(tpl.render(ctx))


def jpcapProcess(list):
    jpcapFlag = ""
    
    completeList = []
    lineList = []
    
    length = len(list)
    z = 0
    lineLength = 0

    while z < len(list) : 
        if list[z] == '03':
            jpcapFlag = ""
            
        elif list[z] == '04':
            jpcapFlag = "_"

        elif list[z] == '0d':
            lineLength = 0
            completeList.append(lineList)
            del lineList[:]
 
        else :
            lineList.append(jpcapFlag + list[z])
            z = z + 1
            lineLength = lineLength + 1
            
            if lineLength > 15:
                lineLength = 0
                completeList.append(lineList)
                del listList[:]    
        
    return completeList

