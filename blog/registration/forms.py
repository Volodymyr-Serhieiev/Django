from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

from .models import User


class LoginForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    password = forms.CharField(label='Password')


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    password_again = forms.CharField(max_length=100, label='Password again', widget=forms.PasswordInput)

    def clean(self):
        password = self.cleaned_data.get('password')
        password_again = self.cleaned_data.get('password_again')
        if password != password_again:
            raise ValidationError('Паролі не збігаються')


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError('Error')
