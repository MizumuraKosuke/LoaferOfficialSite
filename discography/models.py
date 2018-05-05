from django.db import models
from django.utils import timezone

CATEGORY = [
    ('album','album'),
    ('single','single'),
    ('video','video'),
    ('book','book'),
    ('download','download'),
]

class Disc(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    Category = models.CharField(max_length=200, choices=CATEGORY, null=True)
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    MPN = models.CharField(max_length=100, blank=True, null=True)
    release = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=200, default='発売中', blank=True, null=True)
    image = models.ImageField(upload_to='disc/', blank=True, null=True)
    songs = models.TextField(blank=True, null=True)
    catchcopy = models.CharField(max_length=200, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title