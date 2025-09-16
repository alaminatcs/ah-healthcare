from .views import ContactViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', ContactViewSet)
urlpatterns = [
    path('', include(router.urls)),
]