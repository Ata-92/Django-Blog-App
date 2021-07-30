from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
# from blog_app.forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from auth_app.forms import ProfileForm, RegisterForm, UserForm
from django.contrib.auth.decorators import login_required
from auth_app.models import Profile
from post_app.models import Comment, Like, Post, PostView

# Create your views here.

def home_view(request):
    posts = Post.objects.all()
    for post in posts:
        post.comments = Comment.objects.filter(post=post).count()
        post.views = PostView.objects.filter(post=post).count()
        post.likes = Like.objects.filter(post=post).count()
    context = {
        "posts": posts
    }
    return render(request, "auth_app/home.html", context)

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
        # To get username and password to authenticate from here
        username = form.cleaned_data["username"]
        password = form.cleaned_data.get("password1")
        # to here
        # email = form.cleaned_data.get("email")
        # user = User(username=username, email=email)
        # user = User.objects.create(username=username, email=email)
        # user.set_password(password)
        # user.save()
        form.save()
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
            messages.error(request, "Something went wrong!")
            return redirect("login")

    context = {
        "form": form
    }
    return render(request, "auth_app/register.html", context)

# @login_required
def logout_view(request):
    messages.success(request, "Logout successful")
    logout(request)
    return render(request, "auth_app/logout.html")

def about_view(request):
    return render(request, "auth_app/about.html")

def profile_view(request):
    # user = request.user
    # user = get_object_or_404(User, username=request.user)
    user_profile = Profile.objects.get(user=request.user)
    user_info = UserForm(request.POST or None, instance=request.user)
    profile_info = ProfileForm(request.POST or None, request.FILES or None, instance=user_profile)

    if user_info.is_valid() and profile_info.is_valid():
        user_field = user_info.save()

        profile = profile_info.save(commit=False)
        profile.user = user_field
        # Alternative way for request.FILES
        # if "image" in request.FILES:
        #     profile.image = request.FILES["image"]
        profile.save()
        messages.success(request, "Profile updated successfully")
        return redirect("home")

    context = {
        "user_info": user_info,
        "profile_info": profile_info
    }
    return render(request, "auth_app/profile.html", context)
