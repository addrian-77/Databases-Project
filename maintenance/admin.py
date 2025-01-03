from django.contrib import admin

# Register your models here.

from .models import MaintenanceRecord

admin.site.register(MaintenanceRecord)