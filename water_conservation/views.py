from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from database.models import *
from django.http import JsonResponse
from datetime import date
from django.db.models import Sum, Count
import json
import random

#PAGES VIEWS

def homepage_view(request):
    countries_with_projects = (
        Project.objects.values("company_name__country__name")
        .annotate(project_count=Count("id"))
        .order_by("-project_count")
    )
    for rank, country in enumerate(countries_with_projects, start=1):
        country["rank"] = rank

    countries_with_most_water_saving = (
        Project.objects.values("company_name__country__name")
        .annotate(total_savings=Sum("water_savings"))
        .order_by("-total_savings")
    )
    for rank, country in enumerate(countries_with_most_water_saving, start=1):
        country["rank"] = rank

    most_popular_technologies = (
        TechnologyImplemented.objects.values("technology__name")
        .annotate(implementation_count=Count("id"))
        .order_by("-implementation_count")
    )
    for rank, tech in enumerate(most_popular_technologies, start=1):
        tech["rank"] = rank

    context = {
        "countries_with_projects": countries_with_projects,
        "countries_with_most_water_saving": countries_with_most_water_saving,
        "most_popular_technologies": most_popular_technologies,
    }
    print(context)
    return render(request, 'homepage.html', context)

def technologies_view(request):
    technologies = Technology.objects.all()
    technologies_json = [
        {
            "id": tech.id,
            "name": tech.name,
            "description": tech.description,
            "category": {
                "id": tech.category.id,
                "name": tech.category.category_name,
            },
            "manufacturer": {
                "id": tech.manufacturer.id,
                "name": tech.manufacturer.name,  
                "address": tech.manufacturer.address,  
            },
        }
        for tech in technologies
    ]
    return render(request, 'technologies.html', {'technologies': json.dumps(technologies_json), 'categories': Category.objects.all(), 'manufacturers': Manufacturer.objects.all(), 'techniques': ConservationTechnique.objects.all()})

def company_view(request):
    return render(request, 'company.html', {'countries': Country.objects.all()})


def profile_view(request):
    # print(request.user)
    is_logged_in = User.is_authenticated
    if is_logged_in:
        watertips = WaterTip.objects.filter(user=request.user)
        projects = Project.objects.filter(user=request.user)
        return render(request, 'profile.html', {'watertips': watertips, 'projects': projects})
    else:
        return redirect('/')
    
def about_view(request):
    return render(request, 'about.html', {'about_messages': AboutMessages.objects.all()})

def watertips_view(request):
    if request.method == 'POST':
        # Preluăm datele din formular
        tip = request.POST['tip']
        # Creăm un obiect nou
        watertip = WaterTip.objects.create(tip=tip, user=request.user)
        watertip.save()
        # Mesaj de succes și redirecționare către pagina de watertips
        # messages.success(request, 'Water tip added successfully!')
        return redirect('watertips')
    return render(request, 'watertips.html', {'watertips': WaterTip.objects.order_by('?')[:6]})

def projects_view(request):
    return render(request, 'projects.html', {'categories': Category.objects.all(), 'companies': Company.objects.filter(user=request.user), 'technologies': Technology.objects.filter(user=request.user)})

#AUTHENTICATION VIEWS

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Login attempt with email: {email}")  # Debug message in console

        try:
            # Find user by email
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            user = None

        if user and user.check_password(password):  # Check if the password is correct
            auth_login(request, user)  # Log the user in
            messages.success(request, 'Login successful!')
            print("Login successful!")  # Success message in console

            # Redirect to the homepage (or 'index' view)
            return redirect('/')  # Or use 'index' if your homepage is named that
        else:
            messages.error(request, 'Invalid email or password!')
            print("Login failed!")  # Failure message in console

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def signup_view(request):
    if request.method == 'POST':
        # Preluăm datele din formular
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Verificăm dacă parolele se potrivesc
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')

        # Creăm un utilizator nou
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Mesaj de succes și redirecționare către pagina de login
        messages.success(request, 'Account created successfully!')
        return redirect('login')  # Redirecționează către pagina de login

    # Renderizează pagina de signup
    return render(request, 'signup.html')


#OTHER FUNCTIONS

def get_country_data(request):
    country_name = request.GET.get('name')

    if not country_name:
        return JsonResponse({'error': 'No country name provided'}, status=400)

    try:
        # Fetch the country object based on the name
        country = Country.objects.get(name=country_name)
        country_projects = list(
            Project.objects.filter(company_name__country__name=country)
            .values_list("project_name", "water_savings")
            .order_by("-water_savings")
        )
        
        country_companies = list(
            Company.objects.filter(country__name=country)
            .values_list("name", "user__username")
        )

        country_soil_data = list(
            SoilData.objects.filter(country__name=country)
            .values_list("ph_level")
        )
        print(country_projects)
        # Prepare the data to send back
        data = {
            'name': country.name,
            'projects': country_projects,
            'companies': country_companies,
            'soil_data': country_soil_data,
        }
        return JsonResponse({'success': True, 'data': data})

    except Country.DoesNotExist:
        return JsonResponse({'error': 'Country not found'}, status=404)

def get_category_description(request):
    category_name = request.GET.get('category', None)
    if category_name:
        # Fetch the category object (adjust based on your model structure)
        category = Category.objects.get(category_name=category_name)
        return JsonResponse({"description": category.description, "name":category.category_name})  # Assuming `description` is a field in your model
    return JsonResponse({"description": "Category not found."})

def get_category_customization(request):
    category_name = request.GET.get('category', None)
    if category_name:
        # Fetch the category object (adjust based on your model structure)
        category = Category.objects.get(category_name=category_name)
        return JsonResponse({"form": category.customization_form})  # Assuming `description` is a field in your model
    return JsonResponse({"description": "Category not found."})

def submit_project(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User must be logged in'}, status=403)
    category = request.POST.get('category')
    project_name = request.POST.get('projectName')
    company_name = request.POST.get('companyName')
    technology_name = request.POST.get('technologyName')
    description = request.POST.get('description')
    goals = request.POST.get('goals')
    water_savings = request.POST.get('waterSavings')

    additional_data= request.POST.dict()
    keys = list(additional_data.keys())

    additional_data = {key: additional_data[key] for key in keys[8:]}

    print(technology_name)
    print(additional_data)

    if not category or not project_name or not company_name or not description or not goals or not water_savings or not additional_data:
        return JsonResponse({'error': 'Missing required fields'}, status=400)
    
    try:
        company_obj = Company.objects.get(name=company_name)
        category_obj = Category.objects.get(category_name=category)
        technology_obj = Technology.objects.get(name=technology_name)
        project = Project.objects.create(
            user=request.user,
            category=category_obj,
            project_name=project_name,
            company_name=company_obj,
            technology=technology_obj,
            description=description,
            goals=goals,
            water_savings=water_savings,
            additional_customization=additional_data,
        )
        project.save()
        project_obj = Project.objects.get(project_name=project_name)
        technology_implemented_obj = TechnologyImplemented.objects.create(
            technology=technology_obj,
            project=project_obj,
            date=date.today(),
            country=Company.objects.get(name=company_name).country,
        )
        technology_implemented_obj.save()
        return JsonResponse({'success': True, 'message': 'Project added successfully!'})  # Return a success message
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    
def submit_technology(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    category_name = request.POST.get('category')
    manufacturer_name = request.POST.get('manufacturer')
    technique_name = request.POST.get('technique')

    if not name or not description or not category_name or not manufacturer_name or not technique_name:
        return JsonResponse({'error': 'Missing required fields'}, status=400)
    
    try:
        if technique_name == 'add-your-own':
            technique_name = request.POST.get('custom_technique')
        if ConservationTechnique.objects.filter(name=technique_name).exists():
            technique_obj = ConservationTechnique.objects.get(name=technique_name)
        else:
            technique_obj = ConservationTechnique.objects.create(
                name = technique_name,
            )
            technique_obj.save()
            technique_obj = ConservationTechnique.objects.get(name=technique_name)
        category_obj = Category.objects.get(category_name=category_name)
        if manufacturer_name == 'add-your-own':
            manufacturer_name = request.POST.get('custom_manufacturer_name')
            manufacturer_address = request.POST.get('custom_manufacturer_address')
        if Manufacturer.objects.filter(name=manufacturer_name).exists():
            manufacturer_obj = Manufacturer.objects.get(name=manufacturer_name)
        else:
            manufacturer_obj = Manufacturer.objects.create(
                name = manufacturer_name,
                address = manufacturer_address,
            )
            manufacturer_obj.save()
            manufacturer_obj = Manufacturer.objects.get(name=manufacturer_name)
        technology = Technology.objects.create(
            name=name,
            description=description,
            category=category_obj,
            manufacturer=manufacturer_obj,
        )
        technology.save()
        technology = Technology.objects.get(name=name)
        technology_technique_obj = TechnologyTechnique.objects.create(
            technology=technology,
            technique=technique_obj,
        )
        technology_technique_obj.save()
        return redirect('technologies')
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
    
def submit_company(request):
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'User must be logged in'}, status=403)
    name = request.POST.get('name')
    country = request.POST.get('country')
    location = request.POST.get('location')

    print(country)

    if not name or not country or not location:
        return JsonResponse({'error': 'Missing required fields'}, status=400)
    
    try:
        country_obj = Country.objects.get(name=country)
        if Location.objects.filter(name=location).exists():
            location_obj = Location.objects.get(name=location)
            # Object exists, and you can use location_obj
        else:
            # Handle the case where the object does not exist
            location_obj = Location.objects.create(
                country = country_obj,
                name = location,
            )
            location_obj.save()
            location_obj = Location.objects.get(name=location)
        
        company = Company.objects.create(
            user=request.user,
            name=name,
            country=country_obj,
            location=location_obj,
        )
        company.save()
        return redirect('company')
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)