from django.shortcuts import get_object_or_404, redirect, render
from post_app.forms import CommentForm, PostForm
from django.contrib import messages
from post_app.models import Category, Comment, Like, Post, PostView

# Create your views here.

def newpost_view(request):
    post_form = PostForm(request.POST or None, request.FILES or None)
    if post_form.is_valid():
        category_data = post_form.cleaned_data["category"]
        if Category.objects.filter(name=category_data):
            category = Category.objects.get(name=category_data)
        else:
            category = Category.objects.create(name=category_data)

        post = post_form.save(commit=False)
        post.category = category
        post.user = request.user
        post.save()
        messages.success(request, "Post created successfully")
        return redirect("home")

    context = {
        "post_form": post_form
    }
    return render(request, "post_app/newpost.html", context)
