from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    return render(request, 'main/main_page.html')


def about(request):
    return HttpResponse('This should be the about page')


def post(request, post_id):
    return render(request, 'main/post.html', {
        'post_id': post_id,
    })


def comment(request, slug):
    return HttpResponse(f'Add a comment to post id:{slug}')


def create(request):
    return render(request, 'main/create.html')


def update_post(request, slug):
    return HttpResponse(f'This should be post update id:{slug}')


def delete(request, slug):
    return HttpResponse(f'Delete a post id:{slug}')
