from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
# from blog_app.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from auth_app.forms import ProfileForm, RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home_view(request):
    return render(request, "auth_app/home.html")

# def login_view(request):
#     form = LoginForm(request.POST or None)
#     context = {
#         "form": form
#     }
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 messages.success(request, "Login successful")
#                 login(request, user)
#                 return redirect("home")
#             else:
#                 messages.error(request, "Account is not active")
#                 return render(request, "blog_app/login.html", context)
#         else:
#             messages.error(request, "Password or username is wrong!")
#             return render(request, "blog_app/login.html", context)
#     return render(request, "blog_app/login.html", context)

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data["username"]
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password1")
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        # user.save()
        messages.success(request, "Register successful")

        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user:
            if authenticated_user.is_active:
                messages.success(request, "Login successful")
                login(request, authenticated_user)
                return redirect("home")
            else:
                messages.error(request, "Account is not active")
                return redirect("inactive")
        else:
            messages.error(request, "Username or password is wrong!")
            return redirect("login")

    context = {
        "form": form
    }
    return render(request, "auth_app/register.html", context)

@login_required
def logout_view(request):
    messages.success(request, "Logout successful")
    logout(request)
    return render(request, "auth_app/logout.html")

def about_view(request):
    return render(request, "auth_app/about.html")

def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            pass

    form = ProfileForm(request.user)
    context = {
        "form": form
    }
    return render(request, "auth_app/profile.html", context)
