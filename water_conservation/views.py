from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from database.models import *
from django.http import JsonResponse

#PAGES VIEWS

def homepage_view(request):
    return render(request, 'homepage.html')

def technologies_view(request):
    return render(request, 'technologies.html')

def company_view(request):
    return render(request, 'company.html')


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
    return render(request, 'projects.html', {'categories': Category.objects.all(), 'companies': Company.objects.all(), 'technologies': Technology.objects.all()})

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
        
        # Prepare the data to send back
        data = {
            'name': country.name,
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
        return JsonResponse({'success': True, 'message': 'Project added successfully!'})  # Return a success message
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)