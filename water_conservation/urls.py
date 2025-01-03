"""
URL configuration for water_conservation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('maintenance/', include('maintenance.urls')),
    path('projects/', include('projects.urls')),
    path('stakeholders/', include('stakeholders.urls')),
    path('techniques/', include('techniques.urls')),
    path('technologies/', include('technologies.urls')),
    path('training_and_research/', include('training_and_research.urls')),
    path('usage_data/', include('usage_data.urls')),
    path('admin/', admin.site.urls),
]
