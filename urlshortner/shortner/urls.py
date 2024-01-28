from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    ##path('<str:token>', views.get_link, name='get_link'),
    path('get_og_link', views.get_og_link, name='get_og_link')

]