from django.shortcuts import render

from hospitalmanagementapp.models import Doctor, Patient
from hospitalapi.serializers import DoctorSerializer, PatientSerializer

from rest_framework import generics

# Create your views here.
class DoctorListCreate(generics.ListCreateAPIView):
	serializer_class = DoctorSerializer
	queryset = Doctor.objects.all()


class DoctorUpdateRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = DoctorSerializer
	queryset = Doctor.objects.all()
	lookup_field = 'id'



class PatientListCreate(generics.ListCreateAPIView):
	serializer_class = PatientSerializer
	queryset = Patient.objects.all()

class PatientUpdateRetrieveDestroy(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = PatientSerializer
	queryset = Patient.objects.all()
	lookup_field = 'id'