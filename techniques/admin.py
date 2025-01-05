from django.contrib import admin

# Register your models here.
from .models import ConservationTechnique
from .models import WaterTip

admin.site.register(ConservationTechnique)
admin.site.register(WaterTip)