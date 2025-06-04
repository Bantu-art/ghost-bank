from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.views import View
from inertia import render
from .models import CustomUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
import json

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/Login')
    def post(self, request):
        # Try to get data from POST or JSON
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not email or not password:
            try:
                data = json.loads(request.body)
                email = email or data.get('email')
                password = password or data.get('password')
            except Exception:
                pass
        if not email or not password:
            return render(request, 'auth/Login', props={
                'error': 'Email and password are required',
                'email': email or '',
            })
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            response = redirect('home')
            response.status_code = 303  # Inertia expects 303 for SPA redirect
            return response
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
        # Try to get data from POST or JSON
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        if not email or not name or not password:
            try:
                data = json.loads(request.body)
                email = email or data.get('email')
                name = name or data.get('name')
                password = password or data.get('password')
            except Exception:
                pass
        if not email:
            return render(request, 'auth/Register', props={
                'error': 'Email is required',
                'email': email or '',
                'name': name or '',
            })
        if CustomUser.objects.filter(email=email).exists():
            return render(request, 'auth/Register', props={
                'error': 'Email already exists',
                'email': email,
                'name': name,
            })
        user = CustomUser.objects.create_user(email=email, name=name, password=password)
        login(request, user)
        response = redirect('home')
        response.status_code = 303  # Inertia expects 303 for SPA redirect
        return response
