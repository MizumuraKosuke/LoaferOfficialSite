from django.shortcuts import render
from django.utils import timezone
from .models import Biography, Member, Event

def biography(request):
    biography = Biography.objects.get()
    member = Member.objects.all()
    events = Event.objects.filter(published_date__lte=timezone.now()).order_by('date')
    return render(request, 'biography/biography.html', {'biography': biography, 'member': member, 'events': events})
