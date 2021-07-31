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

def details_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.POST.get("like"):
        Like.objects.filter(user=request.user, post=post).delete()
    elif request.POST.get("dislike"):
        Like.objects.create(user=request.user, post=post)
    elif request.POST.get("comment"):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            content = comment_form.cleaned_data["content"]
            Comment.objects.create(user=request.user, post=post, content=content)
            # or
            # comment = comment_form.save(commit=False)
            # comment.user = request.user
            # comment.post = post
            # comment.save()

    PostView.objects.create(user=request.user, post=post)
    comments = Comment.objects.filter(post=post).count()
    views = PostView.objects.filter(post=post).count()
    likes = Like.objects.filter(post=post).count()
    user_like_check = Like.objects.filter(user=request.user, post=post).exists()
    comment_form = CommentForm()
    comment_list = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "views": views,
        "likes": likes,
        "user_like_check": user_like_check,
        "comment_form": comment_form,
        "comment_list": comment_list
    }
    return render(request, "post_app/details.html", context)

def update_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        category_data = form.cleaned_data["category"]
        if Category.objects.filter(name=category_data):
            category = Category.objects.get(name=category_data)
        else:
            category = Category.objects.create(name=category_data)

        post = form.save(commit=False)
        post.category = category
        post.save()
        messages.success(request, "Post updated successfully")
        return redirect("home")
    return render(request, "post_app/update.html", {"form": form})

def delete_view(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully")
        return redirect("home")
    return render(request, "post_app/delete.html", {"post": post})
