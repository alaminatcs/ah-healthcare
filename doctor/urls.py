from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register('specialization/list', views.SpecializationViewSet)
router.register('designation/list', views.DesignationViewSet)
router.register('available_time/list', views.AvailableTimeViewSet)
router.register('list', views.DoctorViewSet, basename='doctor_list')

urlpatterns = [
    path('', include(router.urls))
]