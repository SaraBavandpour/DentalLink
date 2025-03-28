from rest_framework import serializers
from .UserModels import PatientRecord, MyModel

from .ServiceModels import DentalClinicServices

from django import forms

# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = MyModel
#         fields = ('title', 'image')

class PatientRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRecord
        fields = '__all__'  # همه فیلدها را بگیرد
        
class DentalClinicServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DentalClinicServices
        fields = '__all__'  # همه فیلدها را بگیرد