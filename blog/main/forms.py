from django import forms
from django.contrib.auth import get_user_model
from django.forms import CheckboxSelectMultiple

from .models import BlogPost, Comment, Topic

User = get_user_model()


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['headline', 'topics']


class CommentModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['blog_post'].widget = forms.HiddenInput()
        self.fields['author'].widget = forms.HiddenInput()

    class Meta:
        model = Comment
        fields = ['comment', 'author', 'blog_post']


class SearchForm(forms.Form):
    search_field = forms.CharField(label='post')
