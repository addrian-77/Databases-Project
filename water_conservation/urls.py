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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_view, name='homepage'),  # Homepage
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('about/', views.about_view, name='about'),
    path('get_country_data/', views.get_country_data, name='get_country_data'),
    path('get_category_description/', views.get_category_description, name="get_category_description"),
    path('get_category_customization/', views.get_category_customization, name="get_category_customization"),
    path('submit_project/', views.submit_project, name='submit_project'),
    path('watertips/', views.watertips_view, name='watertips'),
    path('projects/', views.projects_view, name='projects'),
    path('admin/', admin.site.urls),
]
