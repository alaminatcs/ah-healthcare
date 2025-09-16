from .models import Service
from rest_framework import viewsets
from .serializers import ServiceSerializer

class ServiceViewset(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer