from django.test import TestCase
from django.urls import reverse
from django.test import Client
from eventfinder.models import EventCategory
from eventfinder.serializer import EventCategorySerializer
from eventfinder.models import Event
from eventfinder.serializer import Event
 
#Test: if all eventCategory from database and from api equal
class EventCategoryTestCase(TestCase):
    def test_eventcategorylist(self):
        url = reverse('eventcategory-list')
        response = self.client.get(url)
        eventCategories = EventCategory.objects.all()
        expected_data = EventCategorySerializer(eventCategories, many=True).data
        assert response.status_code == 200
        self.assertEqual(response.data, expected_data)

#Test: if all event from database and from api equal
class EventTestCase(TestCase):
    def test_eventlist(self):
        url = reverse('event-list')
        response = self.client.get(url)
        events = Event.objects.all()
        expected_data = EventCategorySerializer(events, many=True).data
        assert response.status_code == 200
        self.assertEqual(response.data, expected_data)
