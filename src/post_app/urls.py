from django.urls import path
from post_app.views import newpost_view

urlpatterns = [
    path("newpost/", newpost_view, name="newpost")
]
