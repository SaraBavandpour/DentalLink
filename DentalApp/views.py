from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientRecordSerializer, DentalClinicServicesSerializer
from .UserModels import PatientRecord
from .ServiceModels import DentalClinicServices
from django.http import JsonResponse

class CombinedView(APIView):
    def get(self, request):
        # دریافت و سریالایز کردن اطلاعات بیماران
        patient_records = PatientRecord.objects.all()
        patient_serializer = PatientRecordSerializer(patient_records, many=True)
        
        # بازگرداندن داده‌های بیماران
        return Response({
            "patient_records": patient_serializer.data
        })

    def post(self, request):
        # دریافت داده‌های بیمار و ذخیره آن‌ها
        patient_serializer = PatientRecordSerializer(data=request.data.get("patient"))
        
        if patient_serializer.is_valid():
            patient = patient_serializer.save()  # ذخیره اطلاعات بیمار
            
            # بازگرداندن داده‌های ذخیره‌شده
            return Response({
                "patient": patient_serializer.data
            }, status=status.HTTP_201_CREATED)
        
        # بازگرداندن خطاها در صورت وجود
        return Response({
            "patient_errors": patient_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class SaveServicesWithID(APIView):
    def post(self, request):
        patient_id = request.data.get("patient_id")
        if not patient_id:
            return Response({"error": "Patient ID is missing."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = PatientRecord.objects.get(patient_id=patient_id)
            
            # بررسی وجود رکورد خدمات برای این بیمار
            if DentalClinicServices.objects.filter(Patient=patient).exists():
                return Response({"error": "This patient already has a services record."}, 
                              status=status.HTTP_400_BAD_REQUEST)
                
        except PatientRecord.DoesNotExist:
            return Response({"error": "Patient not found."}, status=status.HTTP_404_NOT_FOUND)

        services_data = request.data.get("services", {})
        
        # ایجاد سریالایزر با context
        service_serializer = DentalClinicServicesSerializer(
            data=services_data,
            context={'patient': patient}
        )

        if service_serializer.is_valid():
            service_serializer.save()
            return Response({
                "message": "Services saved successfully!",
                "services": service_serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "errors": service_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)