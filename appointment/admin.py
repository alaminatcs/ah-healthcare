from django.contrib import admin
from .models import Appointment

# Register your models here.
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'type', 'status', 'patient_symptoms', 'available_time', 'cancel']

    def patient_name(self, obj):
        return obj.patient.user.first_name
    
    def doctor_name(self, obj):
        return obj.doctor.user.first_name

admin.site.register(Appointment, AppointmentModelAdmin)