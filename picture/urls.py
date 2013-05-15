# -*- encoding: utf8 -*-
from django.conf.urls import patterns, include, url
from views import login_view , signin , start_template
import settings
from views import image_explain ,process_img,contact,about , message_book
from loadpicture.views import load_image , upload , process_picture , gray_process

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'picture.views.home', name='home'),
    # url(r'^picture/', include('picture.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
     url( '^assets/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': settings.MEDIA_URL}),
    url( '^img/(?P<path>.*)$', 'django.views.static.serve', 
        { 'document_root': settings.Img_dir}),
            
                       
    url('^$' , signin , name="signin"),
    url('^start_template/$' , start_template , name ="start_template"),
    # just explain why I start this project
    url('^image_explain/$' , image_explain , name = "image_explain"),
    url('^process_img/$' , process_img , name ="process_img"),
    url('^contact/$' , contact , name ="contact"),
    url('^about/$' , about , name ="about"),
    url('^load_image/$' , load_image , name="laod_picture"),
    url('^upload/$' , upload , name="up_data"),
    url('^process_pic/$' , process_picture , name="process_pic"),
    url('^message_book/(?P<page>\w{0,5})' , message_book , name="message_book"),
    url('^gray_process/$' , gray_process , name = "gray_process"),
)
