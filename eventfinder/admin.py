from typing import Any
from django.contrib import admin
from eventfinder.models import (EventCategory, County, Event, EventFavorite, EventAttendance)

class EventCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    ordering = ["name"]
    fields = ['name', 'imageUrlString']

admin.site.register(EventCategory, EventCategoryAdmin)

class CountyAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    ordering = ["name"]
    fields = ['name']

admin.site.register(County, CountyAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "categoryId", "event_date"]
    ordering = ["event_date"]
    fields = ['categoryId', 'countyId','title','event_date',
              'place_name','location_x','location_y','imageUrl','description',
              'ticketPrice','address']
    
    def get_queryset(self, request):
        qs = super(EventAdmin, self).get_queryset(request)
        return qs.filter(author=request.user)
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.author = request.user
        return super(EventAdmin, self).save_model(request, obj, form, change)
    
admin.site.register(Event, EventAdmin)