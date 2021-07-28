from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from auth_app.models import Profile

# class LoginForm(forms.ModelForm):
#     class Meta():
#         model = User
#         fields = ("username", "password")

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta():
        model = User
        fields = ("username", "email")

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ("username", "email")

class ProfileForm(forms.ModelForm):
    class Meta():
        model = Profile
        # fields = ("image", "bio")
        exclude = ("user",)
