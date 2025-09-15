from .models import Patient
from .serializers import PatientSerializer
from rest_framework import viewsets

class PatientViewset(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer