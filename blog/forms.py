from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(label="Email", validators=[EmailValidator], error_messages={"invalid": 'This is invalid email'})
    class Meta:
        model = User
        fields = ('username','email',)


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('bloger',)


class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        exclude = ('users',)





