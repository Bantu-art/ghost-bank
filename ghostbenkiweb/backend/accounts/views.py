from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse
from inertia import render
from .models import CustomUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/Login')  # Updated to match React file

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/Login', props={
                'error': 'Invalid credentials',
                'email': email,
            })

class LogoutView(View):
    @method_decorator(login_required)
    def post(self, request):
        logout(request)
        return redirect('home')

class RegistrationView(View):
    def get(self, request):
        return render(request, 'auth/Register')  # Updated to match React file

    def post(self, request):
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'auth/Register', props={
                'error': 'Email already exists',
                'email': email,
                'name': name,
            })

        user = CustomUser.objects.create_user(email=email, name=name, password=password)
        login(request, user)
        return redirect('home')
