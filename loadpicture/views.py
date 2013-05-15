# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect , HttpResponse
import Image , os
from picture import settings
import ImageFile

# this is for uploading picture
@csrf_exempt
def load_image(request):
    return render_to_response('load_image.html' , context_instance=RequestContext(request))

@csrf_exempt
def upload(request):
    f = request.FILES
    if f.get('docfile') is not None:
        fi = f.get('docfile')
        parser = ImageFile.Parser()
        for chunk in fi.chunks():                
            parser.feed(chunk)  
        img = parser.close()
        name = os.path.join(settings.Img_dir, 'liu.jpg') 
        img.save(name)
        return render_to_response('load_image.html' , context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect("/load_image/")

@csrf_exempt
def process_picture(request):
    pic_name = os.path.join(settings.Img_dir , "liu.jpg")
    new_width =  100
    new_height = 200
    pic_img = Image.open(pic_name)
    pic_img = pic_img.resize((new_width , new_height) , Image.ANTIALIAS)
    new_liu_path = pic_name.replace("liu" , "new_liu")
    pic_img.save(new_liu_path)
    return HttpResponse("load")
    
    
