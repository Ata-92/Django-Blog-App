from django.urls import path

urlpatterns = [
    path("newpost/", newpost_view, name="newpost")
]
