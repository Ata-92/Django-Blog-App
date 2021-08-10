from django.urls import path
from post_app.views import PostDelete, backend_view, details_view, frontend_view, full_stack_view, newpost_view, update_view

urlpatterns = [
    path("newpost/", newpost_view, name="newpost"),
    path("frontend/", frontend_view, name="frontend"),
    path("backend/", backend_view, name="backend"),
    path("full_stack/", full_stack_view, name="full_stack"),
    path("<str:slug>/", details_view, name="details"),
    path("<str:slug>/update/", update_view, name="update"),
    # path("<str:slug>/delete/", delete_view, name="delete"),
    path("<str:slug>/delete/", PostDelete.as_view(), name="delete"),
]
