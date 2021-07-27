from django.urls import path
from auth_app.views import home_view, logout_view, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home_view, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="auth_app/login.html"), name="login"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="auth_app/password_reset.html"), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="auth_app/password_reset_done.html"), name="password_reset_done"),
    path("register/", register_view, name="register"),
    path("inactive/", register_view, name="inactive"),
    path("logout/", logout_view, name="logout")
]
