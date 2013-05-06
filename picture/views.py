# -*-:encoding:utf8 -*-
'''
Created on 2013-1-31

@author: liucumt
'''
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template.context import RequestContext
from django.contrib import auth
from django.http import HttpResponseRedirect , HttpResponse
import Image , settings,os
import time
import datetime
from loadpicture.models import Mesbook
from django.core.paginator import Paginator


@csrf_exempt
def login_view(request):
    return render_to_response('index.html' , context_instance=RequestContext(request))

@csrf_exempt
def signin(request):
    username = request.POST.get('username' , '')
    password = request.POST.get('password' , '')
    user = auth.authenticate(username=username , password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/start_template/')
    else:
        return render_to_response('signin.html' , context_instance=RequestContext(request))
    
@csrf_exempt
def start_template(request):
    return render_to_response('starter_template.html' , context_instance=RequestContext(request))

@csrf_exempt
def image_explain(request):
    img_dir = settings.Img_dir
    save_img=os.path.join(img_dir , 'save_concert.jpg')
    if os.path.exists(save_img):
        os.remove(save_img)
        
    concert = os.path.join(img_dir, 'concert.jpg') 
    img = Image.open(concert)
    new_img = img.convert('L')
    new_img.save(save_img)
    return render_to_response('image_explain.html' , context_instance=RequestContext(request))

@csrf_exempt
def process_img(request):
    pass
    #return render_to_response('hero.html' , context_instance=RequestContext(request))
    
@csrf_exempt
def contact(request):
    return render_to_response('contact.html',context_instance=RequestContext(request))

@csrf_exempt
def about(request):
    return render_to_response('about.html',context_instance=RequestContext(request))

@csrf_exempt
def message_book(request , page =''):
    bt_method = request.method
    dic_text = {}
    if bt_method == "POST":
        text_mes = request.POST.get("mes_book_text")
        time_mes = datetime.datetime.now()
        text = Mesbook.objects.create(mestext = text_mes , mestime = time_mes)
        text.save()
        
        mes_all = Mesbook.objects.all()
        mes_page = Paginator(mes_all , 4)
        last_page = mes_page.num_pages
        first_mes_page = mes_page.page(1)
        return render_to_response("message_book.html",
                {"mes_tx":first_mes_page ,"page":page, "last_page":last_page} , context_instance = RequestContext(request))
     
    mes_all = Mesbook.objects.all()
    mes_page = Paginator(mes_all , 4)
    last_page = mes_page.num_pages
    first_mes_page = mes_page.page(page)
    return render_to_response("message_book.html" , {"mes_tx":first_mes_page ,
        "page":page,"last_page":last_page} , context_instance =RequestContext(request))
    
    
