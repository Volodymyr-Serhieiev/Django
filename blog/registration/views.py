from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from .forms import AuthenticationForm
from django.contrib.auth import login, get_user_model, logout

User = get_user_model()


def profile(request, username):
    return HttpResponse(f'{username} profile')


def change_password(request):
    return HttpResponse('Password change page')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = User(username=form.cleaned_data['username'])
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('/')
        return render(request, 'registration/registration.html', context={'form': form})
    form = RegistrationForm()
    return render(request, 'registration/registration.html', context={'form': form})


def my_logout(request):
    logout(request)
    return redirect('login')


def my_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('/')

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
