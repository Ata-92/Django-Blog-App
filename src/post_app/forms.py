from django import forms
from django.db.models import fields
from django.forms import widgets
from post_app.models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = ["name"]
        labels = {"name": "Category"}
        widgets = {
            "name": forms.Select(attrs={"class": "form-select"})
        }

class PostForm(forms.ModelForm):
    STATUSES = (("Draft", "Draft"), ("Published", "Published"))
    status = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select"}), choices=STATUSES)
    class Meta():
        # STATUSES = (("Draft", "Draft"), ("Published", "Published"))
        model = Post
        exclude = ("user", "category", "slug")
        # fields = ("title", "content", "image", "status")
        # widgets = {
        #     "title": forms.TextInput(attrs={"class": "form-control"}),
        #     "content": forms.Textarea(attrs={"class": "form-control"}),
        #     "image": forms.FileInput(attrs={"class": "form-control"}),
        #     "status": forms.Select(choices=STATUSES, attrs={"class": "form-select"})
        # }
