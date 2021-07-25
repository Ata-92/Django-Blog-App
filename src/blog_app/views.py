from django.shortcuts import redirect, render
from blog_app.forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home_view(request):
    return render(request, "blog_app/home.html")
