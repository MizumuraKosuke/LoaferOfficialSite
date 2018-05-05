from django.shortcuts import render
from django.utils import timezone
from .models import Media

def media(request):
    next_medias = Media.objects.filter(published_date__lte=timezone.now()).order_by('date').reverse().filter(date__gte=timezone.now())
    past_medias = Media.objects.filter(published_date__lte=timezone.now()).order_by('date').reverse().filter(date__lt=timezone.now())
    return render(request, 'media/media.html', {'next_medias': next_medias, 'past_medias': past_medias})