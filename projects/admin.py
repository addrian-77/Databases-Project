from django.contrib import admin

# Register your models here.
from .models import Country
from .models import Location
from .models import Project
from .models import Feedback

admin.site.register(Country)
admin.site.register(Location)
admin.site.register(Project)
admin.site.register(Feedback)