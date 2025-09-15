from .models import Service
from .serializers import ServiceSerializer
from rest_framework import viewsets

class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer