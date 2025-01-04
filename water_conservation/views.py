from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        greeting = request.POST.get('say', 'Hi')
        recipient = request.POST.get('to', 'World')
        if greeting and recipient:
            result = f"You entered: {greeting}, {recipient}"
        else:
            result = ""
        return render(request, 'homepage.html', {'result': result})
    return render(request, 'homepage.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
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
