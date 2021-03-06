from django.urls import path
from auth_app.views import about_view, home_view, logout_view, profile_view, register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home_view, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="auth_app/login.html"), name="login"),
    path("password_reset/", auth_views.PasswordResetView.as_view(template_name="auth_app/password_reset.html"), name="password_reset"),
    path("password_reset_done/", auth_views.PasswordResetDoneView.as_view(template_name="auth_app/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="auth_app/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="auth_app/password_reset_complete.html"), name='password_reset_complete'),
    path("register/", register_view, name="register"),
    path("inactive/", register_view, name="inactive"),
    path("logout/", logout_view, name="logout"),
    path("about/", about_view, name="about"),
    path("profile/", profile_view, name="profile"),
]
