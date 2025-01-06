from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from techniques.models import WaterTip
from projects.models import Country
from django.http import JsonResponse

def index_view(request):
    return render(request, 'homepage.html')

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

def profile_view(request):
    is_logged_in = User.is_authenticated
    # print("user logged in")
    if is_logged_in:
        return render(request, 'profile.html')
    else:
        return redirect('/')
    
def about_view(request):
    return render(request, 'about.html')

def watertips_view(request):
    if request.method == 'POST':
        # Preluăm datele din formular
        tip = request.POST['tip']
        # Creăm un obiect nou
        watertip = WaterTip.objects.create(tip=tip)
        watertip.save()
        # Mesaj de succes și redirecționare către pagina de watertips
        # messages.success(request, 'Water tip added successfully!')
        return redirect('watertips')
    return render(request, 'watertips.html', {'watertips': WaterTip.objects.order_by('?')[:6]})

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
