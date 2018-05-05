from django.shortcuts import render
from django.utils import timezone
import os,sys
sys.path.append(os.pardir)
from live.models import Live

def home(request):
    next_lives = Live.objects.filter(published_date__lte=timezone.now()).order_by('date').reverse().filter(date__gte=timezone.now())
    return render(request, 'home/home.html', {'next_lives': next_lives})
