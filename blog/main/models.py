from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

user = get_user_model()


class Topic(models.Model):
    headline = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)
    authors = models.ManyToManyField(user, blank=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return f'{self.headline}'


def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
    if not self.id:
        self.slug = slugify(self.headline)
    super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class BlogPost(models.Model):
    headline = models.CharField(max_length=12, blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey(user, on_delete=models.SET_NULL, blank=True, null=True)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return f'{self.headline}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            self.slug = slugify(self.headline)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)


class Author(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    comment = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey(user, on_delete=models.SET_NULL, blank=True, null=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment}'
