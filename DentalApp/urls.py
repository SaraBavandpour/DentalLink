from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CombinedView


urlpatterns = [
    path('PersonView/', CombinedView.as_view(), name='PersonView')
   
]
