## Basic URL Configurations
from unicodedata import name
from django.urls import path, include
## Import routers
from rest_framework import routers
## Import everything from views
from .views import *

## Define Router
router = routers.DefaultRouter()

## Define router paths and viewset to be used

router.register(r'api/weather', WeatherViewSet, basename='weather-data')
router.register(r'api/weather/stats', WeatherStatsViewSet, basename='weather-stats')

## specify URL path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]