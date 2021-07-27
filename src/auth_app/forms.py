from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields

# class LoginForm(forms.ModelForm):
#     class Meta():
#         model = User
#         fields = ("username", "password")

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ("username", "email")
