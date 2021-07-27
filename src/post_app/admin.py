from django.contrib import admin

from post_app.models import Category, Comment, Like, Post, PostView

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(PostView)
