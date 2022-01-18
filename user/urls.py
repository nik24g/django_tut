from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='home'),
    path('aboutUs', views.about, name='about'),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name="logout")
]
