from django.shortcuts import get_object_or_404, redirect, render
from post_app.forms import CommentForm, PostForm
from django.contrib import messages
from post_app.models import Category, Comment, Like, Post, PostView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

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
    if request.method == "POST" and not request.user.is_authenticated:
        return redirect("login")
    elif request.POST.get("like"):
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

    if request.user.is_authenticated:
        PostView.objects.create(user=request.user, post=post)
        post.user_like_check = Like.objects.filter(user=request.user, post=post).exists()
    else:
        post.user_like_check = False
    post.comments = Comment.objects.filter(post=post).count()
    post.views = PostView.objects.filter(post=post).count()
    post.likes = Like.objects.filter(post=post).count()
    post.comment_form = CommentForm()
    post.comment_list = Comment.objects.filter(post=post)

    context = {
        "post": post,
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

# def delete_view(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     if request.method == "POST":
#         post.delete()
#         messages.success(request, "Post deleted successfully")
#         return redirect("home")
#     return render(request, "post_app/delete.html", {"post": post})

class PostDelete(DeleteView):
    model = Post
    template_name = "post_app/delete.html"  #  default  "app/modelName.lower()_confirm_delete.html" = "fscohort/student_confirm_delete.html"
    success_url = reverse_lazy("home")

def frontend_view(request):
    posts = Post.objects.filter(category__name="Frontend")
    for post in posts:
        post.comments = Comment.objects.filter(post=post).count()
        post.views = PostView.objects.filter(post=post).count()
        post.likes = Like.objects.filter(post=post).count()
    context = {
        "posts": posts
    }
    return render(request, "auth_app/home.html", context)

def backend_view(request):
    posts = Post.objects.filter(category__name="Backend")
    for post in posts:
        post.comments = Comment.objects.filter(post=post).count()
        post.views = PostView.objects.filter(post=post).count()
        post.likes = Like.objects.filter(post=post).count()
    context = {
        "posts": posts
    }
    return render(request, "auth_app/home.html", context)

def full_stack_view(request):
    posts = Post.objects.filter(category__name="Full Stack")
    for post in posts:
        post.comments = Comment.objects.filter(post=post).count()
        post.views = PostView.objects.filter(post=post).count()
        post.likes = Like.objects.filter(post=post).count()
    context = {
        "posts": posts
    }
    return render(request, "auth_app/home.html", context)
