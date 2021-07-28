from django import forms
from post_app.models import Post

class PostForm(forms.ModelForm):
    CATEGORIES = (("Option 1", "Frontend"), ("Option 2", "Backend"), ("Option 3", "Full Stack"))
    STATUSES = (("Option 1", "Draft"), ("Option 2", "Published"))
    category = forms.ChoiceField(choices=CATEGORIES)
    status = forms.ChoiceField(choices=STATUSES)
    class Meta():
        model = Post
        exclude = ("user",)
