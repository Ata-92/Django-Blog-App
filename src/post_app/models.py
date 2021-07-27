from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_images", blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, blank=True)
    # slug = models.IntegerField()
    slug = models.SlugField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_tamp =models.IntegerField()
