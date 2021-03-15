from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import PostMonster, PostSurvivor
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class SurvivorPageView(ListView):
    model = PostSurvivor
    template_name = 'survivor.html'
    context_object_name = 'lista_posts'

class MonstersPageView(ListView):
    model = PostMonster
    template_name = 'monster.html'
    context_object_name = 'lista_posts'

class ConfigPageView(TemplateView):
    template_name = 'config.html'