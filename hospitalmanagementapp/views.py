from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


from hospitalmanagementapp.mixins import GroupRequiredMixin
from hospitalmanagementapp.filters import DoctorFilter, PatientFilter
from hospitalmanagementapp.models import Doctor, Patient
from hospitalmanagementapp.forms import DoctorForm, PatientForm

# Create your views here.
class LoginRequiredMixin(object):
	def  dispatch(self, request, *args, **kwargs):
		user = self.request.user
		if user.is_authenticated:
			pass
		else:
			return redirect('accounts:login-page')
		return super().dispatch(request, *args, **kwargs)


class DashboardPage(LoginRequiredMixin,TemplateView):
	template_name = 'hospitalmanagementapp/base.html'
	success_url = reverse_lazy('accounts:home-page')


#doctor crud
class DoctorList(GroupRequiredMixin,ListView):
	template_name = 'doctor/doctor_list.html'
	context_object_name = 'doctor_list'
	model = Doctor
	group_required = ['Doctor']
	paginate_by = 1

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['doctor_filter'] = DoctorFilter(self.request.GET, queryset=self.get_queryset())
		return context



class DoctorCreate(GroupRequiredMixin,SuccessMessageMixin,LoginRequiredMixin,CreateView):
	template_name = 'doctor/doctor_create.html'
	success_url = reverse_lazy('hospitalmanagementapp:doctor-create')
	form_class = DoctorForm
	success_message = "Doctor Information is created"
	group_required = ['Doctor']


	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_message(self, cleaned_data):
		return self.success_message % cleaned_data

	def get_initial(self):
		return {'name':'dafs','address':'wersd','email':'adsw@gmail.com'}


class DoctorUpdate(GroupRequiredMixin,SuccessMessageMixin, UpdateView):
	template_name = 'doctor/doctor_update.html'
	form_class = DoctorForm
	success_url = reverse_lazy('hospitalmanagementapp:doctor-list')
	success_message = "Doctor Update Successfull"
	group_required = ['Doctor']


	def form_valid(self, form):
		form.save()
		return super().form_valid(form)

	def get_success_message(self, cleaned_data):
		return self.success_message % cleaned_data

	def get_object(self, **kwargs):
		id = self.kwargs.get('id')
		return get_object_or_404(Doctor, id=id)


class DoctorDelete(GroupRequiredMixin,SuccessMessageMixin, DeleteView):
	template_name = 'doctor/doctor_delete.html'
	success_message = 'Doctor Information is deleted'
	success_url = reverse_lazy('hospitalmanagementapp:doctor-list')
	group_required = ['Doctor']


	def get_object(self, **kwargs):
		id = self.kwargs.get('id')
		return get_object_or_404(Doctor, id = id)

	def get_success_message(self, cleaned_data):
		return self.success_message % cleaned_data


#patient crud
class PatientList(GroupRequiredMixin,ListView):
	template_name = 'patient/patient_list.html'
	model = Patient
	context_object_name = 'patient_list'
	group_required = ['Patient']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['patient_filter'] = PatientFilter(self.request.GET, self.get_queryset())
		return context


class PatientCreate(GroupRequiredMixin,SuccessMessageMixin,CreateView):
	template_name = 'patient/patient_create.html'
	success_message = 'Patient Register Successfull'
	success_url = reverse_lazy('hospitalmanagementapp:patient-create')
	form_class = PatientForm
	group_required = ['Patient']

	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_message(self, cleaned_data):
		return self.success_message % cleaned_data


class PatientUpdate(GroupRequiredMixin,SuccessMessageMixin, UpdateView):
	template_name = 'patient/patient_update.html'
	success_message = 'Patient Update Successfull'
	success_url = reverse_lazy('hospitalmanagementapp:patient-list')
	form_class = PatientForm
	group_required = ['Patient']

	def form_valid(self, form):
		return super().form_valid(form)

	def get_success_message(self, cleaned_data):
		return self.success_message % cleaned_data

	def get_object(self, **kwargs):
		id = self.kwargs.get('id')
		return get_object_or_404(Patient, id=id)

class PatientDelete(GroupRequiredMixin,SuccessMessageMixin, DeleteView):
	template_name = 'patient/patient_delete.html'
	success_message = 'Patient Information is deleted'
	success_url = reverse_lazy('hospitalmanagementapp:patient-list')
	group_required = ['Patient']

	def get_object(self, **kwargs):
		id = self.kwargs.get('id')
		return get_object_or_404(Patient, id=id)

	def get_success_message(self, cleaned_data):
		return self.success_message % cleaned_data