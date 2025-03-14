from django.contrib import admin

# Register your models here.

from .models import PatientRecord

admin.site.register(PatientRecord)
