## Import Django Rest Framework Viewsets. Here I will use Viewsets
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
## Import rest framework pagination to get paginated response
from rest_framework.pagination import PageNumberPagination
import logging

## Import Serializers defined. This converts data to JSON
from .serializers import WeatherSerializer, WeatherStatsSerializer
from .models import Weather, WeatherStats

## Using logger to logs info for the API
logging.basicConfig(filename='project/logs/log_process.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger("mylogger")

# Create your views here.


class WeatherViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset  = Weather.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            return paginator.get_paginated_response(WeatherSerializer(page, many=True).data)
        else:
            return Response(WeatherSerializer(queryset, many=True).data)
     
     
    @action(methods=['GET'], detail=False, url_path=r'filter/station_id=(?P<station_id>\w+)')        
    def retrive_stationID(self, request, station_id=None):
        queryset = Weather.objects.filter(station_id=station_id)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            return paginator.get_paginated_response(WeatherSerializer(page, many=True).data)
        else:
            return Response(WeatherSerializer(queryset, many=True).data)
        
        
    @action(methods=['GET'], detail=False, url_path=r'filter/date=(?P<date>\w+)')    
    def retrive_date(self, request, date=None):
        date = date[:4] + '-' + date[4:6] + '-' + date[6:]
        queryset = Weather.objects.filter(date=date)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            return paginator.get_paginated_response(WeatherSerializer(page, many=True).data)
        else:
            return Response(WeatherSerializer(queryset, many=True).data)


class WeatherStatsViewSet(viewsets.ViewSet):

    def list(self, request):
        
        queryset = WeatherStats.objects.all()
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            return paginator.get_paginated_response(WeatherStatsSerializer(page, many=True).data)
        else:
            serializer = WeatherStatsSerializer(queryset, many=True)
            return Response(serializer.data)
        
        
    @action(methods=['GET'], detail=False, url_path=r'filter/station_id=(?P<station_id>\w+)')    
    def retrieve_stationID(self, request, station_id=None):
        queryset = WeatherStats.objects.filter(station_id=station_id)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        page = paginator.paginate_queryset(queryset, request)
        if page is not None:
            serializer = WeatherStatsSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            serializer = WeatherStatsSerializer(queryset, many=True)
            return Response(serializer.data)
    