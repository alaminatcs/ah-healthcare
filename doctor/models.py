from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient
from .constants import STAR_CHOICES

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    time_slot = models.CharField(max_length=100)

    def __str__(self):
        return self.time_slot

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='doctor/images/', blank=True, null=True)
    specializations = models.ManyToManyField(Specialization)
    designations = models.ManyToManyField(Designation)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_me = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"

class Review(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    comments = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=20, choices=STAR_CHOICES, default='☆☆☆☆☆')

    class Meta:
        unique_together = ('patient', 'doctor')


    def __str__(self):
        return f"Patient: {self.patient.user.first_name}; Doctor: {self.doctor.user.first_name}"
