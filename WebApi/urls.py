"""
URL configuration for WebApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from eventfinder.views import EventCategoryViewSet
from eventfinder.views import CountyViewSet
from eventfinder.views import EventViewSet
from eventfinder.views import EventFavoriteViewSet
from eventfinder.views import EventAttendenceViewSet
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


router = DefaultRouter()
router.register(r'eventcategory', EventCategoryViewSet, basename='eventcategory')
router.register(r'eventcounty', CountyViewSet, basename='eventcounty')
router.register(r'event', EventViewSet, basename='event')
router.register(r'eventfavorite', EventFavoriteViewSet, basename='eventfavorite')
router.register(r'eventattendence', EventAttendenceViewSet, basename='eventattendence')

urlpatterns = [ 
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += router.urls
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
