from django.urls import path
from . import views

urlpatterns = [
    path('', views.discography, name='discography'),
    path('<int:disc_id>', views.disc_detail, name='disc_detail'),
    path('album/', views.album, name='album'),
    path('single/', views.single, name='single'),
    path('video_disc/', views.video_disc, name='video_disc'),
    path('book/', views.book, name='book'),
    path('download/', views.download, name='download'),
]