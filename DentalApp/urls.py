from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CombinedView , SaveServicesWithID


urlpatterns = [
    path('PersonView/', CombinedView.as_view(), name='PersonView'),
    path('save-services/', SaveServicesWithID.as_view(), name='SaveServicesWithID'),
   
]
