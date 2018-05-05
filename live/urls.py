from django.urls import path
from . import views

urlpatterns = [
    path('', views.live, name='live'),
    path('<int:live_id>', views.live_detail, name='live_detail'),
]