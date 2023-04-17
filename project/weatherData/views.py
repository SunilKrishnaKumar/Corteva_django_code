from curses.ascii import HT
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def getWeather(request):
    message = f'Done'
    return HttpResponse(message)

def getWeatherStats(request):
    message = f'TODO'
    return HttpResponse(message)
