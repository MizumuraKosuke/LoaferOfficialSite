from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from .models import Live, LiveContact
from .forms import LiveContactForm

def live(request):
    next_lives = Live.objects.filter(published_date__lte=timezone.now()).order_by('date').reverse().filter(date__gte=timezone.now())
    past_lives = Live.objects.filter(published_date__lte=timezone.now()).order_by('date').reverse().filter(date__lt=timezone.now())
    if request.method == "POST":
        form = LiveContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            subject = post.name + 'さんからライブ予約が入りました。'
            message='NAME: ' + post.name + '\nmail adress: ' + post.mail_address + '\n\n公演名: ' + post.which_live + '\n枚数: ' + str(post.ticket) + '枚'
            from_email = post.mail_address
            to = [
                settings.EMAIL_HOST_USER,
            ]
            send_mail(subject, message, from_email, to)
    else:
        form = LiveContactForm()
    return render(request, 'live/live.html', {'next_lives': next_lives, 'past_lives': past_lives, 'form': form})

def live_detail(request, live_id):
    live = get_object_or_404(Live, pk=live_id)
    if request.method == "POST":
        form = LiveContactForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            subject = post.name + 'さんからライブ予約が入りました。'
            message='NAME: ' + post.name + '\nmail adress: ' + post.mail_address + '\n\n公演名: ' + post.which_live + '\n枚数: ' + str(post.ticket) + '枚'
            from_email = post.mail_address
            to = [
                settings.EMAIL_HOST_USER,
            ]
            send_mail(subject, message, from_email, to)
    else:
        form = LiveContactForm()
    return render(request, 'live/live_detail.html', {'live': live, 'form': form})