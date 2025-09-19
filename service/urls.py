from .views import ServiceViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('services', ServiceViewset, basename='services')

app_name='service'
urlpatterns = [
    path('', include(router.urls)),
]