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
    
    
    
