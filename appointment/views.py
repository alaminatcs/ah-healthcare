from . import models
from . import serializers
from rest_framework import viewsets, permissions

# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    # custom query for patient-wise appointment list
    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id=patient_id)
        return queryset
    
    # custom query for doctor-wise appointment list
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     doctor_id = self.request.query_params.get('doctor_id')
    #     if doctor_id:
    #         queryset = queryset.filter(doctor_id=doctor_id)
    #     return queryset