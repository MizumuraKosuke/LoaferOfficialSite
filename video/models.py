from django.db import models
from django.utils import timezone

class Video(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    URL = models.URLField(blank=True, null=True)
    explain = models.TextField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def embed(self):
        input_url = self.URL
        start = input_url.find('watch?v=')
        end = input_url.find('&')
        if start != -1 or end != -1:
            self.URL = 'https://www.youtube.com/embed/' + input_url[start+8:end]
            self.save()

    def __str__(self):
        return self.title

