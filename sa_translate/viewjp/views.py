# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from binascii import unhexlify

from models import translateText, Text
import re
from StringIO import StringIO

def mainview(request) :
    tpl = loader.get_template('viewjp/mainview.html')
    ctx = RequestContext(request, {})
    return HttpResponse(tpl.render(ctx))

def viewText(request, number=1):
    entries = Text.objects.get(textNumber = number)
    
    parsedText = re.findall('f...|..', entries.hexString)
    text = jpcapProcess(parsedText)
    
    translatedText = callTextlist(number)
    
    tpl = loader.get_template('viewjp/viewjp.html')
    ctx = RequestContext(request, {'text':text, 'list':parsedText, 'number':number, 'translatedText':translatedText})
    return HttpResponse(tpl.render(ctx))

def callTextlist(number):
    entries = translateText.objects.filter(textNumber = int(number)).order_by('-transDate')
    
    return entries

def viewList(request, page=1):
    entries = Text.objects.all()
    paginator = Paginator(entries, 50)
    
    try:
        currentPage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        currentPage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        currentPage = paginator.page(paginator.num_pages)
    
    return render_to_response('viewjp/listview.html', {"currentpage": currentPage})

def allList(request):
    entries = Text.objects.all()
    
    return render_to_response('viewjp/alllist.html', {"entries": entries})

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
    author = request.POST.get('author')
    
    translatedText = translateText(textNumber=number, Contents=text, userID=author)
    translatedText.save()
    
    return redirect('/surgingaura/viewtext/' + number)


def downloadIps(request):
    ADD_TEXT_POS = 2293760 #번역되는 텍스트가 롬에 추가될 위치
    HANJA_POINTER = 426588 #한자가 위치하는 부분
    FONT_POSITION = 2097153

    patchList = []
    patchList.append('\x50\x41\x54\x43\x48')
    
    patchList.append('\x06\x82\x5d\x00\x03\x20\x00\x00')
    entries = translateText.objects.get(textNumber = 621)
    entries2 = Text.objects.get(textNumber = 621)
    
    stringList = re.findall("..", hex((int(entries.Contents.encode("euc-kr").encode("hex"),16) - 0xb0a0)))
    stringList = stringList[2:]
    
    textPtr = "%06x" % entries2.textPos
    patchList.append(unhexlify(textPtr))
    
    textLength = "\x00\x03"
    patchList.append(textLength)
    
    textContents = "\x23\x00\x00"
    patchList.append(textContents)
    
    textPos = "\x23\x00\x00"
    patchList.append(textPos)  
     
    textLength = "%04x" % (len(entries.Contents.encode("euc-kr") ) + 62)
    patchList.append(unhexlify(textLength))
    
    
    z = 0

    
    while z < len(stringList):
        if len(stringList[z]) == 2:
            hex_string = hex(61440 + (int(stringList[z][0], 16) * 94) + (int(stringList[z][1], 16) - 1))
            hex_string = hex_string[2:]
        else:
            hex_string = stringList[z].encode("hex")

        patchList.append(unhexlify(hex_string))
        z = z + 1
    
    
    patchList.append('\x45\x4f\x46')
    
    patchList = "".join(patchList)
    
    ips = StringIO()
    
    ips.write(patchList)
    
    
    response = HttpResponse(mimetype="application/ips")
    response["Content-Disposition"] = "attachment; filename=sao.ips"
    
    response.write(ips.getvalue())
    
    return response
    