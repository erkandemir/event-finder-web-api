from rest_framework import serializers
from eventfinder.models import EventCategory, County, Event, EventAttendance, EventFavorite
from django.contrib.auth.models import User

class EventCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = ['id', 'name', 'imageUrlString']

class EventCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'categoryId', 'countyId', 'title', 'event_date', 'place_name',
                  'location_x', 'location_y', 'imageUrl', 'description', 'ticketPrice', 'address']
        
class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = ['id', 'userDeviceId', 'eventId']

class EventAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendance
        fields = ['id', 'userDeviceId', 'eventId']


class EventFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventFavorite
        fields = ['id', 'userDeviceId', 'eventId']







