from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, "blog_app/home.html")
