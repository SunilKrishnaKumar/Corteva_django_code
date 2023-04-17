from dataclasses import fields
from rest_framework import serializers
## Imported serialisers
from .models import Weather, WeatherStats

## This converts models into JSON format. I used Model Serializer 
## as it takes defaults from the model defintion

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('station_id', 'date', 'max_temp', 'min_temp', 'precipitation')
        # fields = "__all__"
        
        
class WeatherStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStats
        fields = ('station_id', 'avg_max_temp', 'avg_min_temp', 'total_precipitation')
        # fields = "__all__"