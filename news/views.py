from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import News

def news(request):
    newss = News.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request, 'news/news.html', {'newss': newss})

def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news': news})