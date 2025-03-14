from django.db import models

# Create your models here.
import uuid
#from mongoengine import Document, fields

from django.db import models

# Create your models here.

class PatientRecord(models.Model):
    patient_id = models.UUIDField(
        primary_key=True,  # می‌توانید آن را به عنوان کلید اصلی تنظیم کنید
        default=uuid.uuid4,  # مقدار پیش‌فرض که UUID به صورت خودکار تولید می‌شود
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
    
    image_file = models.ImageField(upload_to='radiology_images/')  # محل ذخیره تصویر
    upload_date = models.DateTimeField(auto_now_add=True)  # تاریخ آپلود
    description = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "Patient Record"
        

class DentalClinicServices(models.Model):
    # Treatment Services
    cavity_filling = models.BooleanField(default=False, verbose_name="Cavity Filling")
    root_canal = models.BooleanField(default=False, verbose_name="Root Canal")
    tooth_extraction = models.BooleanField(default=False, verbose_name="Tooth Extraction")
    gum_treatment = models.BooleanField(default=False, verbose_name="Gum Treatment")
    
    # Cosmetic Services
    teeth_whitening = models.BooleanField(default=False, verbose_name="Teeth Whitening")
    laminates = models.BooleanField(default=False, verbose_name="Laminates")
    composite = models.BooleanField(default=False, verbose_name="Composite")
    smile_design = models.BooleanField(default=False, verbose_name="Smile Design")
    
    # Restorative Services
    implants = models.BooleanField(default=False, verbose_name="Dental Implants")
    dental_prosthetics = models.BooleanField(default=False, verbose_name="Dental Prosthetics")
    crown_and_bridges = models.BooleanField(default=False, verbose_name="Crowns and Bridges")
    
    # Orthodontic Services
    fixed_orthodontics = models.BooleanField(default=False, verbose_name="Fixed Orthodontics")
    removable_orthodontics = models.BooleanField(default=False, verbose_name="Removable Orthodontics")
    
    # Preventive Services
    scaling_and_polishing = models.BooleanField(default=False, verbose_name="Scaling and Polishing")
    fluoride_therapy = models.BooleanField(default=False, verbose_name="Fluoride Therapy")
    sealants = models.BooleanField(default=False, verbose_name="Sealants")

    # Other Services
    online_consultation = models.BooleanField(default=False, verbose_name="Online Consultation")
    appointment_reminders = models.BooleanField(default=False, verbose_name="Appointment Reminders")
    
    # General Information
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation Date")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Update Date")

    def __str__(self):
        return "Dental Clinic Services"


class ServiceSchedule(models.Model):
    service = models.ForeignKey(DentalClinicServices, on_delete=models.CASCADE, related_name="schedules")
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    available_date = models.DateField(verbose_name="Available Date")
    
    def __str__(self):
        return f"{self.service.service_name} - {self.available_date} ({self.start_time} to {self.end_time})"
