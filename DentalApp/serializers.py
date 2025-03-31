from rest_framework import serializers
from .UserModels import PatientRecord, MyModel
from .ServiceModels import DentalClinicServices
from django import forms

class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = '__all__'  # همه فیلدها را بگیرد
        
class DentalClinicServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DentalClinicServices
        fields = '__all__'
        extra_kwargs = {
            'Patient': {'read_only': True}  # اجازه ندهید از طریق سریالایزر بیمار تغییر کند
        }

    def create(self, validated_data):
        # بیمار از context دریافت می‌شود
        patient = self.context['patient']
        validated_data['Patient'] = patient
        return super().create(validated_data)