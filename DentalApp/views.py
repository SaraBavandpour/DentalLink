
# def upload_image(request):
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ImageForm()
#     return render(request, 'upload_image.html', {'form': form})


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PatientRecordSerializer, DentalClinicServicesSerializer
from .UserModels import PatientRecord
from .ServiceModels import DentalClinicServices

class CombinedView(APIView):
    def get(self, request):
        # نمایش اطلاعات موجود
        patient_records = PatientRecord.objects.all()
        clinic_services = DentalClinicServices.objects.all()
        
        patient_serializer = PatientRecordSerializer(patient_records, many=True)
        service_serializer = DentalClinicServicesSerializer(clinic_services, many=True)
        
        # بازگرداندن داده‌های هر دو مدل
        return Response({
            "patient_records": patient_serializer.data,
            "clinic_services": service_serializer.data
        })

    def post(self, request):
        # ذخیره اطلاعات بیماران
        patient_serializer = PatientRecordSerializer(data=request.data.get("patient"))
        service_serializer = DentalClinicServicesSerializer(data=request.data.get("services"))
        
        if patient_serializer.is_valid() and service_serializer.is_valid():
            patient = patient_serializer.save()  # ذخیره بیمار
            service_serializer.save(Patient=patient)  # ذخیره خدمات مرتبط با بیمار
            
            return Response({
                "patient": patient_serializer.data,
                "services": service_serializer.data
            }, status=status.HTTP_201_CREATED)
        
        # در صورت وجود خطا
        errors = {
            "patient_errors": patient_serializer.errors,
            "service_errors": service_serializer.errors
        }
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)
