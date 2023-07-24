from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action
from eventfinder.models import EventCategory, County, Event, EventAttendance, EventFavorite
from eventfinder.serializer import (EventCategorySerializer, EventSerializer, 
                                    EventCountySerializer, EventFavoriteSerializer, EventAttendanceSerializer)


class EventCategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = EventCategory.objects.all()
    serializer_class = EventCategorySerializer

class CountyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser]
    queryset = County.objects.all()
    serializer_class = EventCountySerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['categoryId', 'event_date']

    @action(detail=True, methods=['get'],url_path='attendence_count', url_name='attendence_count')
    def getAttendenceCount(self, request, pk=None):
        event = self.get_object()
        if event is not None:
            count = Event.objects.filter(eventattendance__eventId = event.id).count()
            return Response({"'eventId' : {eventId} 'attendenceCount': {count}".format(eventId= event.id, count=count)})
        return None
    

class EventFavoriteViewSet(viewsets.ModelViewSet):
    queryset = EventFavorite.objects.all()
    serializer_class = EventFavoriteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['userDeviceId']

class EventAttendenceViewSet(viewsets.ModelViewSet):
    queryset = EventAttendance.objects.all()
    serializer_class = EventAttendanceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['eventId']


    
