from django.db import models
from django.utils import timezone

class Biography(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='biography/biography', blank=True, null=True)

    def __str__(self):
        return self.text


class Member(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)
    part = models.CharField(max_length=50)
    age = models.IntegerField(default=0, blank=True, null=True)
    image = models.ImageField(upload_to='biography/member', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name


class Event(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    date = models.DateField(null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
