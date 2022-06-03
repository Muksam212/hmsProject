from django.urls import path

from hospitalapi.views import DoctorListCreate,DoctorUpdateRetrieveDestroy,PatientListCreate,PatientUpdateRetrieveDestroy

app_name = 'hospitalapi'

urlpatterns = [
	path('api/doctor',DoctorListCreate.as_view(), name='doctor-list'),
	path('api/doctor/<int:id>/',DoctorUpdateRetrieveDestroy.as_view(), name='doctor-update-delete'),

	path('api/patient/', PatientListCreate.as_view(), name='patient-list'),
	path('api/patient/<int:id>/',PatientUpdateRetrieveDestroy.as_view(), name='patient-update-delete')
]