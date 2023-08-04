from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet 
from rest_framework.decorators import action
from datetime import datetime, timedelta, time
from eventfinder.models import EventCategory, County, Event, EventAttendance, EventFavorite
from eventfinder.serializer import (EventCategorySerializer, EventSerializer, 
                                    EventCountySerializer, EventFavoriteSerializer, EventAttendanceSerializer)


class EventCategoryViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer

class CountyViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = County.objects.all()
    serializer_class = EventCountySerializer

class EventViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    queryset = Event.objects.all()
    filterset_fields = {'categoryId':  ['exact'],
                         'event_date': ['gte', 'lte', 'exact']}
    serializer_class = EventSerializer
   
    @action(detail=True, methods=['get'],url_path='attendence_count', url_name='attendence_count')
    def getAttendenceCount(self, request, pk=None):
        event = self.get_object()
        if event is not None:
            count = Event.objects.filter(eventattendance__eventId = event.id).count()
            return Response({"'eventId' : {eventId} 'attendenceCount': {count}".format(eventId= event.id, count=count)})
        return None
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["userdeviceid"] = self.request.query_params.get('userdeviceid')
        return context
        
    
        
class EventFavoriteViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = EventFavorite.objects.all()
    serializer_class = EventFavoriteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['userDeviceId','eventId']


class EventAttendenceViewSet(ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['eventId']


    
