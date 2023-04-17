from django.urls import path
from .views import getWeather

urlpatterns = [
    path('', getWeather)
]