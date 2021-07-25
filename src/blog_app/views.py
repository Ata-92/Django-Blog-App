from django.contrib import messages
from django.shortcuts import redirect, render
# from blog_app.forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.

def home_view(request):
    return render(request, "blog_app/home.html")

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
