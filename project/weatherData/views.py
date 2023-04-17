# from curses.ascii import HT
# from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import logging

from .serializers import WeatherSerializer, WeatherStatsSerializer
from .models import Weather, WeatherStats

logging.basicConfig(filename='project/logs/log_process.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger("mylogger")

# Create your views here.

# class WeatherViewSet(viewsets.ModelViewSet):
#     queryset = Weather.objects.all()
#     serializer_class = WeatherSerializer
#     logger.info("queryset", type(queryset))

# class WeatherViewSet(viewsets.GenericViewSet):
#     def list(self, request):
#         queryset = Weather.objects.all()
#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = WeatherSerializer(page, many=True)
#             return self.get_paginated_response(serializer.data)
#         else:
#             serializer = WeatherSerializer(queryset, many=True)
#             return Response(serializer.data)

class WeatherViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset  = Weather.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer =  WeatherSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = WeatherSerializer(queryset, many=True)
            return Response(serializer.data)
    
# class WeatherStatsViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = WeatherStats.objects.all()
#         serializer = WeatherStatsSerializer(queryset, many=True)
#         return Response(serializer.data)


class WeatherStatsViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = WeatherStats.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = WeatherStatsSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = WeatherStatsSerializer(queryset, many=True)
            return Response(serializer.data)

# class WeatherStatsViewSet(APIView):
#     def get(self, request):
#         queryList = WeatherStats.objects.all().values()
#         # serializer = WeatherStatsSerializer(queryset, many=True)
#         return Response(queryList)

# class WeatherStatsViewSet(viewsets.ModelViewSet):
#     queryset = WeatherStats.objects.all()
#     serializer_class = WeatherStatsSerializer
#     # logger.info("queryset", type(queryset))
    