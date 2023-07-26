from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


#Event Category Model
class EventCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    imageUrlString = models.TextField()
    def __str__(self):
        return self.name

#Event County Model
class County(models.Model):
    name = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.name

#Event Model
class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollment_users', null=True)
    categoryId = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='category_set')
    countyId = models.ForeignKey(County, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    event_date = models.DateField()
    place_name = models.CharField(max_length=100)
    location_x = models.DecimalField(max_digits=9999, decimal_places=8)
    location_y = models.DecimalField(max_digits=9999, decimal_places=8)
    imageUrl = models.TextField()
    description = models.TextField()
    ticketPrice = models.DecimalField(max_digits=9, decimal_places=2, null=True)
    address = models.TextField()
    def __str__(self):
        return self.title

#Event Attendance Model
class EventAttendance(models.Model):
    userDeviceId = models.TextField()
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

#Event Favorite Model
class EventFavorite(models.Model):
    userDeviceId = models.TextField()
    eventId = models.ForeignKey(Event, on_delete=models.CASCADE)

