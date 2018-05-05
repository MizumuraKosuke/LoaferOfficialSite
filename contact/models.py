from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True)
    mail_address = models.EmailField(null=True)
    message = models.TextField(null=True)
