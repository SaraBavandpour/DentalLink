
from django.db import models
#from .models import MyModel

# Create your models here.

class PatientRecord(models.Model):
    patient_id = models.AutoField(
        primary_key=True,  # می‌توانید آن را به عنوان کلید اصلی تنظیم کنید
        editable=False  # کاربر نمی‌تواند این فیلد را تغییر دهد
    )

    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    #تاریخچه درمان 
    medical_history = models.TextField(null=True, blank=True)
    #آلرژی ها
    allergies = models.TextField(null=True, blank=True)
    #دارو های فعلی
    current_medications = models.TextField(null=True, blank=True)
    #درمان های قبلی
    previous_treatments = models.TextField(null=True, blank=True)
    
    #image_file = models.ImageField(upload_to='radiology_images/')  # محل ذخیره تصویر
    #upload_date = models.DateTimeField(auto_now_add=True)  # تاریخ آپلود
    #description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "Patient Record"
        

class MyModel(models.Model):
    field_name = models.CharField(max_length=100)
