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
    fav_data = serializers.SerializerMethodField()
    class Meta:
        model = Event
        fields = ['id', 'categoryId', 'countyId', 'title', 'event_date', 'place_name',
                  'location_x', 'location_y', 'imageUrl', 'description', 'ticketPrice', 'address', 'fav_data']
        
        

    def get_fav_data(self, obj):
        _userdeviceid = self.context.get('userdeviceid')
        favourites = EventFavorite.objects.filter(eventId__id = obj.id, userDeviceId =_userdeviceid)
        if(favourites.count() > 0):
            return EventFavoriteSerializer(favourites[0]).data
        else:
            return None
        
        
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







