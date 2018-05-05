from django.db import models
from django.utils import timezone

class News(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(default=timezone.now, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
