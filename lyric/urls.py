from django.urls import path
from . import views

urlpatterns = [
    path('', views.lyric, name='lyric'),
]