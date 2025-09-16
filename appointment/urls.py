from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('list', views.AppointmentViewset)
urlpatterns = [
    path('', include(router.urls))
]