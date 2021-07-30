from django.urls import path
from post_app.views import details_view, newpost_view

urlpatterns = [
    path("newpost/", newpost_view, name="newpost"),
    path("<str:slug>/", details_view, name="details"),
    # path("<str:slug>/update", update_view, name="update"),
    # path("<str:slug>/delete/", delete_view, name="delete")
]
