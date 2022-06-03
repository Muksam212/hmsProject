from django.db import models
from django.contrib.auth.models import User

# Create your models here.
GENDER = (
		('MALE','MALE'),
		('FEMALE','FEMALE'),
	)

SPECIALIST = (
		('HEART','HEART'),
		('ANESTHESIOLOGY','ANESTHESIOLOGY'),
		('DERMATOLOGY','DERMATOLOGY'),
		('MEDICAL GENETICS','MEDICAL GENETICS')

	)


class Doctor(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=100)
	photo = models.ImageField(upload_to='hospitalmanagementapp/doctor/images')
	email = models.EmailField()
	ph_number = models.PositiveIntegerField('phone_number')
	specialist = models.CharField(max_length=100, choices=SPECIALIST)
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Doctors'


	def __str__(self):
		return "{}".format(self.name)



class Patient(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	gender = models.CharField(max_length=100,choices=GENDER)
	photo = models.ImageField(upload_to='hospitalmanagementapp/patient/images')
	address = models.CharField(max_length=100)
	email = models.EmailField(null=True, blank=True)
	ph_number = models.PositiveIntegerField('phone_number')
	date_created = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name_plural = 'Patients'

	def __str__(self):
		return "{}".format(self.user)
