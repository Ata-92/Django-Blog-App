from django.urls import path
from blog_app.views import home_view

urlpatterns = [
    path("", home_view, name="home")
]
