from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return HttpResponse('This should be the home page')


def about(request):
    return HttpResponse('This should be the about page')


def post(request, slug):
    return HttpResponse(f'This should be post id:{slug}')


def comment(request, slug):
    return HttpResponse(f'Add a comment to post id:{slug}')


def create(request):
    return HttpResponse(f'Create a new post')


def update_post(request, slug):
    return HttpResponse(f'This should be post update id:{slug}')


def delete(request, slug):
    return HttpResponse(f'Delete a post id:{slug}')
