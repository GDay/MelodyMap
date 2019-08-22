from django.db import models
from django.conf import settings

class Instrument(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Advert(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lon = models.FloatField()
    lat = models.FloatField()
    is_band = models.BooleanField(default=True)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    instruments = models.ManyToManyField(Instrument)

    def __str__(self):
        return self.title

