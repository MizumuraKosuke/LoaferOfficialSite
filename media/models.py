from django.db import models
from django.utils import timezone

CATEGORY = [
    ('TV','TV'),
    ('Radio','Radio'),
    ('Magazine','Magazine'),
    ('Web', 'Web'),
    ('Other','Other')
]

class Media(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    Category = models.CharField(max_length=200, choices=CATEGORY, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(blank=True, null=True)
    broadcast = models.CharField(max_length=100, blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
