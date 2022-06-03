import django_filters
from hospitalmanagementapp.models import Doctor


class DoctorFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(lookup_expr= 'icontains')

	class Meta:
		model = Doctor
		fields = ['name']

class PatientFilter(django_filters.FilterSet):
	address = django_filters.CharFilter(lookup_expr='iexact')

	class Meta:
		model = Doctor
		fields = ['address']