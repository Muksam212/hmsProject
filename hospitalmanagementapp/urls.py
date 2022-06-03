from django.urls import path
from hospitalmanagementapp.views import (DashboardPage,DoctorCreate,DoctorList,DoctorUpdate,DoctorDelete, PatientCreate, 
								PatientList,PatientUpdate, PatientDelete)

from .import views



app_name = 'hospitalmanagementapp'

urlpatterns = [
	path('dashboard/',DashboardPage.as_view(), name='dashboard-page'),

	#doctor curd
	path('doctorCreate/', DoctorCreate.as_view(), name='doctor-create'),
	path('doctorList/', DoctorList.as_view(), name='doctor-list'),
	path('doctor/<int:id>/update/',DoctorUpdate.as_view(), name='doctor-update'),
	path('doctor/<int:id>/delete/', DoctorDelete.as_view(), name='doctor-delete'),


	#patient crud
	path('patientCreate/', PatientCreate.as_view(), name='patient-create'),
	path('patientList/',PatientList.as_view(), name='patient-list'),
	path('patient/<int:id>/update/', PatientUpdate.as_view(), name='patient-update'),
	path('patient/<int:id>/delete/', PatientDelete.as_view(), name='patient-delete'),
]