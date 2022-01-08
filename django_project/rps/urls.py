from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='rps-home'),
    path('about/', views.about,name='rps-about'),

]

