from . import models
from . import serializers
from rest_framework import viewsets, filters

# Create your views here.
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class DesignationViewSet(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

# filter available time for specific doctor
class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor = doctor_id)
        return queryset

class AvailableTimeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AvailableTimeSerializer
    queryset = models.AvailableTime.objects.all()
    filter_backends = [AvailableTimeForSpecificDoctor]

    def get_queryset(self):
        return super().get_queryset()

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)