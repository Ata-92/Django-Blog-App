from django.urls import path
from post_app.views import delete_view, details_view, newpost_view, update_view

urlpatterns = [
    path("newpost/", newpost_view, name="newpost"),
    path("<str:slug>/", details_view, name="details"),
    path("<str:slug>/update/", update_view, name="update"),
    path("<str:slug>/delete/", delete_view, name="delete")
]
