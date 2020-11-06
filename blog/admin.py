from django.contrib import admin
from .models import Post


@admin.register(Post)
class Posts(admin.ModelAdmin):
    list_display = ['title', 'content']
