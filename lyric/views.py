from django.shortcuts import render
from django.utils import timezone
from .models import Lyric

def lyric(request):
    lyrics = Lyric.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'lyric/lyric.html', {'lyrics': lyrics})

