from django.db import models

# Create your models here.

class Weather(models.Model):
    station_id = models.CharField(max_length=255)
    date = models.DateField()
    max_temp = models.IntegerField()
    min_temp = models.IntegerField()
    precipitation = models.IntegerField()
