from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Manufacturer
from .models import Technology
from .models import TechnologyImplemented
from .models import TechnologyTechnique

admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Technology)
admin.site.register(TechnologyImplemented)
admin.site.register(TechnologyTechnique)
