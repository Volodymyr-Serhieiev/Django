from django.db import models


class Topic(models.Model):
    headline = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)
    authors = models.ManyToManyField('Author', blank=True)

    def __str__(self):
        return f'{self.headline}'


class BlogPost(models.Model):
    headline = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, blank=True, null=True)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
        return f'{self.headline}'


class Author(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'
