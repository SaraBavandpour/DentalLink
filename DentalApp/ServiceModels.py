from django.db import models
from .UserModels import PatientRecord


class DentalClinicServices(models.Model):
    service_id = models.AutoField(
        primary_key=True,  # می‌توانید آن را به عنوان کلید اصلی تنظیم کنید
        editable=False  # کاربر نمی‌تواند این فیلد را تغییر دهد
    )
    Patient = models.ForeignKey(  # تغییر از OneToOne به ForeignKey
        PatientRecord,
        on_delete=models.CASCADE
    )
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
