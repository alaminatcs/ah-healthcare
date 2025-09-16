from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['patient_username', 'doctor_username', 'type', 'status', 'patient_symptoms', 'available_time', 'cancel']

    def patient_username(self, obj):
        return obj.patient.user
    
    def doctor_username(self, obj):
        return obj.doctor.user

admin.site.register(Appointment, AppointmentModelAdmin)