# NOT NEEDED ANYMORE
from django.db import models


class Location(models.Model):
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()