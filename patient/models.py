from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='patient/images/', blank=True, null=True)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.user.first_name