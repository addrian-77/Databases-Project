from django.shortcuts import render

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
