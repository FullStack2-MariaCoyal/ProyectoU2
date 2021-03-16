from django.urls import path
from .views import HomePageView, SurvivorPageView, MonstersPageView, UploadPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('monsters/', MonstersPageView.as_view(), name = 'monster'),
    path('survivor/', SurvivorPageView.as_view(), name = 'survivor'),
    path('upload/', UploadPageView, name = 'upload')

]