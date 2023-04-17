from django.db import models

# Create your models here.

class Weather(models.Model):
    station_id = models.CharField(max_length=255)
    date = models.DateField()
    max_temp = models.IntegerField(null=True)
    min_temp = models.IntegerField(null=True)
    precipitation = models.IntegerField(null=True)
    
class WeatherStats(models.Model):
    station_id = models.CharField(max_length=255)
    avg_max_temp = models.DecimalField(max_digits=6, decimal_places= 3, null=True)
    avg_min_temp = models.DecimalField(max_digits=6, decimal_places= 3, null=True)
    total_precipitation = models.DecimalField(max_digits=10, decimal_places= 3, null=True)
