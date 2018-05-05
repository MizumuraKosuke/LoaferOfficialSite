from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Live(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    open_time = models.TimeField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    adv = models.IntegerField(default=0, blank=True, null=True)
    door = models.IntegerField(default=0, blank=True, null=True)
    artists = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='live/', blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

live_list = Live.objects.filter(published_date__lte=timezone.now()).order_by('date').reverse().filter(date__gte=timezone.now())

LIVE=[]
for live in live_list:
    LIVE.append((live.title,live.title))

class LiveContact(models.Model):
    name = models.CharField(max_length=200, null=True)
    mail_address = models.EmailField(null=True)
    which_live = models.CharField(max_length=200, choices=LIVE, null=True)
    ticket = models.IntegerField(default=1, validators=[MaxValueValidator(100), MinValueValidator(1)] ,null=True)
