from django import forms
from hospitalmanagementapp.models import Doctor, Patient
import django_filters

class DoctorForm(forms.ModelForm):
	class Meta:
		model = Doctor
		fields = ['name','address','email','ph_number','specialist','photo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['name'].widget.attrs.update({
				'class':'form-control',
			})
		for field in self.fields:
			self.fields[field].widget.attrs.update({
					'class':'form-control',
				})
		self.fields['photo'].widget.attrs.update({
				'class':'form-control',
				'onchange':'loadFile(event)',
			})


class PatientForm(forms.ModelForm):
	class Meta:
		model = Patient
		fields = ['user','gender','address','email','ph_number','photo']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['address'].widget.attrs.update({
				'class':'form-control',
			})
		for field in self.fields:
			self.fields[field].widget.attrs.update({
					'class':'form-control',
				})
		self.fields['photo'].widget.attrs.update({
				'class':'form-control',
				'onchange':'loadFile(event)',
			})


