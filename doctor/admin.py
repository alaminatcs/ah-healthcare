from django.contrib import admin
from .models import Specialization, Designation, AvailableTime, Doctor

# Register your models here.
class SpecializationsModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Specialization, SpecializationsModelAdmin)

class DesignationsModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Designation, DesignationsModelAdmin)
admin.site.register(AvailableTime)
admin.site.register(Doctor)