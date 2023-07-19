from django.http import HttpResponse
from django.shortcuts import render


def profile(request, username):
    return HttpResponse(f'{username} profile')


def change_password(request):
    return HttpResponse('Password change page')


def registration(request):
    return render(request, 'registration/registration.html')


def login(request):
    return render(request, 'registration/login.html')


def logout(request):
    return HttpResponse('Logout')
