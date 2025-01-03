from django.contrib import admin

# Register your models here.
from .models import TrainingProgram
from .models import ResearchStudy

admin.site.register(TrainingProgram)
admin.site.register(ResearchStudy)