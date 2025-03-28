from django.contrib import admin

# Register your models here.

from .UserModels import PatientRecord

admin.site.register(PatientRecord)
