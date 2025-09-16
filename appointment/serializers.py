from .models import Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField(many=False)
    patient = serializers.StringRelatedField(many=False)
    available_time = serializers.StringRelatedField(many=False)
    class Meta:
        model = Appointment
        fields = '__all__'