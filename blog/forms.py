from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BlogPost,User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model: User
        fields = ['username','name','password1','password2']

class UserLoginForm(AuthenticationForm):
    class Meta:
        model:User
        fields = ['username','password']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']