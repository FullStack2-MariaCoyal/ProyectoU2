from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import PostMonster, PostSurvivor
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import UploadImage

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        base = 'static/img/'
        fs = FileSystemStorage(location=base,base_url=base)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')

class HomePageView(TemplateView):
    template_name = 'home.html'

class SurvivorPageView(ListView):
    model = PostSurvivor
    template_name = 'survivor.html'
    context_object_name = 'lista'

class MonstersPageView(ListView):
    model = PostMonster
    template_name = 'monster.html'
    context_object_name = 'lista'