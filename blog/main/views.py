from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import BlogPostModelForm, CommentModelForm, SearchForm
from .models import BlogPost, Comment, Topic


def home_page(request, slug=None):
    posts = BlogPost.objects.all()
    topics = Topic.objects.all()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            if slug:
                posts = BlogPost.objects.filter(headline__icontains=form.cleaned_data['search_field'], topics_slug=slug)
            else:
                posts = BlogPost.objects.filter(headline__icontains=form.cleaned_data['search_field'])
            return render(request, 'main/main_page.html', {
                'posts': posts,
                'form': form,
                'topics': topics
            })
    form = SearchForm()
    return render(request, 'main/main_page.html', {
        'posts': posts,
        'form': form,
        'topics': topics

    })


def about(request):
    return HttpResponse('This should be the about page')


@login_required(login_url='login')
def post(request, slug):
    blog_post = BlogPost.objects.get(slug=slug)
    topics = [topic.headline for topic in blog_post.topics.all()]
    comments = Comment.objects.filter(blog_post=blog_post)
    if request.method == 'POST':
        form = CommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return render(request, 'main/post.html', {
                'headline': f'headline - {blog_post.headline}',
                'created_at': f'created_at - {blog_post.created_at}',
                'author': f'author - {blog_post.author}',
                'comments': comments,
                'topics': f'topics - {", ".join(topics)}',
                'form': form

            })
        return render(request, 'main/post.html', {
            'headline': f'headline - {blog_post.headline}',
            'created_at': f'created_at - {blog_post.created_at}',
            'author': f'author - {blog_post.author}',
            'comments': comments,
            'topics': f'topics - {", ".join(topics)}',
            'form': form

        })
    form = CommentModelForm(initial={'blog_post': blog_post, 'author': request.user})
    return render(request, 'main/post.html', {
        'headline': f'headline - {blog_post.headline}',
        'created_at': f'created_at - {blog_post.created_at}',
        'author': f'author - {blog_post.author}',
        'comments': comments,
        'topics': f'topics - {", ".join(topics)}',
        'form': form

    })


class PostCreate(View):
    @login_required(login_url='login')
    def get(self, request):
        form = BlogPostModelForm()
        return render(request, 'main/post_create_form.html', context={'form': form})

    @login_required(login_url='login')
    def post(self, request):
        form = BlogPostModelForm(request.POST)
        print(request.POST['topics'])
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            form.save_m2m()
            return render(request, 'main/post_form_was_valid.html', {'post_name': blog_post})
        return render(request, 'main/post_create_form.html', {'form': form})


class PostCreateView(CreateView):
    template_name = 'main/post_create_form.html'
    model = BlogPost
    fields = ['headline', 'topics', 'author']


def update_post(request, slug):
    return HttpResponse(f'This should be post update id:{slug}')


def delete(request, slug):
    return HttpResponse(f'Delete a post id:{slug}')
