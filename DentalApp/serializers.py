from rest_framework import serializers
from .models import PatientRecord

class GenericSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'  # همه فیلدها را بگیرد