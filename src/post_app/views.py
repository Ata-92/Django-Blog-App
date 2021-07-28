from django.shortcuts import redirect, render
from post_app.forms import PostForm
from django.contrib import messages

# Create your views here.

def newpost_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Post created successfully")
        return redirect("home")
    return render(request, "post_app/newpost.html", {"form": form})
