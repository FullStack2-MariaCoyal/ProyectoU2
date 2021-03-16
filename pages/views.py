from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import PostMonster, PostSurvivor
# Create your views here.
from django.shortcuts import render

from .forms import UploadImage

def UploadPageView(request):
    if request.method == 'POST':
        
        print(request)
        form = UploadImage(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "Image uploaded succesfully!"
    else:
        form = UploadImage()
    context = {'foo': 'bar'}
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