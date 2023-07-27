from django.contrib import admin

from .models import Topic, BlogPost, Author, Comment


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['headline', 'created_at']
    filter_horizontal = ['authors']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['headline', 'author', 'created_at']
    filter_horizontal = ['topics']


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'blog_post', 'created_at']
