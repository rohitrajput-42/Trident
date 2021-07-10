from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms import ModelForm
from .models import Post

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs = {'class': 'form-control'}),
            'password1': forms.TextInput(attrs = {'class': 'form-control'}),
            'password2': forms.TextInput(attrs = {'class': 'form-control'}),
        }

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text']

        widget = {
            'text': forms.TextInput(attrs = {'class': 'form-control'})
        }