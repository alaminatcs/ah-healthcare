from .models import Patient
from rest_framework import serializers

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'