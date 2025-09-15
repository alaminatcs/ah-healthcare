from .views import PatientViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', PatientViewset)
urlpatterns = [
    path('', include(router.urls)),
]