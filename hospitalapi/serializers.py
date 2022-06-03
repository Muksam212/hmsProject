from rest_framework import serializers
from hospitalmanagementapp.models import Doctor, Patient

class DoctorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Doctor
		fields = ['id','name','address','email','ph_number','photo','specialist','date_created']


class PatientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Patient
		fields = ['id','user','gender','address','email','photo','ph_number','date_created']