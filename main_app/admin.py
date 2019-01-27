from django.contrib import admin
from .models import NewPost, Comment

# Register your models here.
admin.site.register(NewPost)
admin.site.register(Comment)