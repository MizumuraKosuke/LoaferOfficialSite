from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Disc

def discography(request):
    discs = Disc.objects.filter(published_date__lte=timezone.now()).order_by('release').reverse()
    return render(request, 'discography/discography.html', {'discs': discs})

def disc_detail(request, disc_id):
    disc = get_object_or_404(Disc, pk=disc_id)
    return render(request, 'discography/disc_detail.html', {'disc': disc})

def album(request):
    album = Disc.objects.filter(published_date__lte=timezone.now()).order_by('release').reverse().filter(Category='album')
    return render(request, 'discography/album.html', {'album': album})

def single(request):
    single = Disc.objects.filter(published_date__lte=timezone.now()).order_by('release').reverse().filter(Category='single')
    return render(request, 'discography/single.html', {'single': single})

def video_disc(request):
    video = Disc.objects.filter(published_date__lte=timezone.now()).order_by('release').reverse().filter(Category='video')
    return render(request, 'discography/video_disc.html', {'video': video})

def book(request):
    book = Disc.objects.filter(published_date__lte=timezone.now()).order_by('release').reverse().filter(Category='book')
    return render(request, 'discography/book.html', {'book': book})

def download(request):
    download = Disc.objects.filter(published_date__lte=timezone.now()).order_by('release').reverse().filter(Category='download')
    return render(request, 'discography/download.html', {'download': download})