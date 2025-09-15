from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='service/images/')
    descriptions = models.TextField()

    def __str__(self):
        return f"Service Type: {self.name}"
