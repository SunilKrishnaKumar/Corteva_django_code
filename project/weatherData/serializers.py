from dataclasses import fields
from rest_framework import serializers

from .models import Weather, WeatherStats

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        # fields = ('id','station_id', 'date', 'max_temp', 'min_temp', 'precipitation')
        fields = "__all__"
        
        
class WeatherStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherStats
        # fields = ('id','station_id', 'avg_max_temp', 'avg_min_temp', 'total_precipitation')
        fields = "__all__"