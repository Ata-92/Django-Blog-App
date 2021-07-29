from django.shortcuts import redirect, render
from post_app.forms import CategoryForm, PostForm
from django.contrib import messages
from post_app.models import Category, Post

# Create your views here.

def newpost_view(request):
    post_form = PostForm(request.POST or None, request.FILES or None)
    category_form = CategoryForm(request.POST or None)
    if post_form.is_valid() and category_form.is_valid():
        category_data = category_form.cleaned_data["name"]
        if Category.objects.filter(name=category_data):
            category = Category.objects.get(name=category_data)
        else:
            category = category_form.save()

        post = post_form.save(commit=False)
        post.category = category
        post.user = request.user
        post.save()
        messages.success(request, "Post created successfully")
        return redirect("home")
    context = {
        "post_form":post_form,
        "category_form":category_form
    }
    return render(request, "post_app/newpost.html", context)
