from django.contrib import admin
from hospitalmanagementapp.models import *
# Register your models here.
admin.site.register([Doctor, Patient])