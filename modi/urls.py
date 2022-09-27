from fnmatch import translate
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('translate/', views.translate, name="translate"),
    path('translated_data/', views.translated_data, name="translated_data")
]