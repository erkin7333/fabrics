from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .models import User


class UserRegistration(View):
    """User registration."""

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)


    def get(self, request):
        form = RegistrationForm()
        context = {
            'form': form
        }
        return render(request, 'account/sing-up.html', context=context)


    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            del data['confirm']
            user = User(**data)
            user.set_password(data['password'])
            user.save()
            return redirect('user_account:login')
        context = {
            'form': form
        }
        return render(request, 'account/sing-up.html', context=context)


def user_login(request):
    """User login."""
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('fabrics_main:homepage')
            form.add_error('password', "Username yoki parol noto'g'ri")

    return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    """User Logot"""
    logout(request)
    return redirect('fabrics_main:homepage')