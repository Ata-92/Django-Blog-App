from django.urls import path
from django.views.generic.base import TemplateView
from blog_app.views import home_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home_view, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="blog_app/login.html"), name="login")
]
