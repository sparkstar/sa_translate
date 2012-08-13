# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader

from models import translateText, Text
import re

def mainview(request) :
    tpl = loader.get_template('viewjp/mainview.html')
    ctx = RequestContext(request, {})
    return HttpResponse(tpl.render(ctx))

def viewText(request, number):
    entries = Text.objects.get(textNumber = number)
    
    parsedText = re.findall('f...|..', entries.hexString)
    text = jpcapProcess(parsedText)
    
    translatedText = callTextlist(number)
    
    tpl = loader.get_template('viewjp/viewjp.html')
    ctx = RequestContext(request, {'text':text, 'list':parsedText, 'number':number, 'translatedText':translatedText})
#    ctx = RequestContext(request, {})
    return HttpResponse(tpl.render(ctx))

def callTextlist(number):
    entries = translateText.objects.filter(textNumber = int(number)).order_by('-transDate')
    
    return entries
    

def jpcapProcess(list):
    jpcapFlag = ""
    
    completeList = []
    lineList = []
    
    z = 0
    lineLength = 0

    while z < len(list) : 
        if list[z] == '03':
            jpcapFlag = ""
            
        elif list[z] == '04':
            jpcapFlag = "_"

        elif list[z] == '0d' or list[z] == '00':
            lineLength = 0
            completeList.append(lineList[:])
            del lineList[:]
            
        elif list[z] == '0c' or list[z] == '0f':
            pass
        
 
        else :
            if list[z] >= '60' :
                lineList.append(jpcapFlag + list[z])
                lineLength = lineLength + 1
            elif list[z] < '60' :
                lineList.append(list[z])
                lineLength = lineLength + 1
            
            
            if lineLength > 15:
                lineLength = 0
                completeList.append(lineList[:])
                del lineList[:]    
        z = z + 1
    return completeList

def translatePost(request):
    text = request.POST.get('translateText')
    number = request.POST.get('number')
    
    translatedText = translateText(textNumber=number, Contents=text)
    translatedText.save()
    
    return HttpResponse("저장 완료")
