from django.contrib import admin

# Register your models here.
from .models import Stakeholder
from .models import FundingSource
from .models import Regulation

admin.site.register(Stakeholder)
admin.site.register(FundingSource)
admin.site.register(Regulation)