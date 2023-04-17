from django.urls import path
from .views import getWeather, getWeatherStats

urlpatterns = [
    path('', getWeather),
    path('stats/', getWeatherStats)
]