import environ
env = environ.Env()
from . import constants
from django.contrib import admin
from .models import Appointment
from django.template.loader import render_to_string
from django.core.mail import send_mail

# Register your models here.
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display = ['patient_username', 'doctor_username', 'type', 'status', 'patient_symptoms', 'available_time', 'cancel']

    def patient_username(self, obj):
        return obj.patient.user
    
    def doctor_username(self, obj):
        return obj.doctor.user
    
    def save_model(self, request, obj, form, change):
        obj.save()

        if obj.status == 'Pending':
            mail_subject = 'Dr. Appointment Request'
            mail_message = constants.request_msg
            meet_link = ''
        elif obj.status == 'Running':
            mail_subject = 'Dr. Appointment Confirmations'
            mail_message = ''
            meet_link = render_to_string('confirm.html')

        send_mail(
            subject = mail_subject,
            message = mail_message,
            recipient_list = [obj.patient.user.email],
            from_email = env('EMAIL_HOST_USER'),
            html_message = meet_link
        )

        return super().save_model(request, obj, form, change)

admin.site.register(Appointment, AppointmentModelAdmin)