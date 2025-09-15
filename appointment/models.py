from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
from .constants import APPOINTMENT_STATUS, APPOINTMENT_TYPE

# Create your models here.
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    available_time = models.OneToOneField(AvailableTime, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=APPOINTMENT_TYPE, default='Online')
    status = models.CharField(max_length=20, choices=APPOINTMENT_STATUS, default='Pending')
    patient_symptoms = models.TextField()
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Dr. {self.doctor.user.first_name}, Patient: {self.patient.user.first_name}"