from django.shortcuts import render
from django.utils import timezone
from .models import Video

def video(request):
    videos = Video.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    for video in videos:
        video.embed()
    return render(request, 'video/video.html', {'videos': videos})
