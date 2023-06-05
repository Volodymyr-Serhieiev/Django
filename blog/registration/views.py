from django.http import HttpResponse
from django.shortcuts import render


def profile(request, username):
    return HttpResponse(f'{username} profile')


def change_password(request):
    return HttpResponse('Password change page')


def register(request):
    return HttpResponse('User registration')


def login(request):
    return HttpResponse('Login')


def logout(request):
    return HttpResponse('Logout')
