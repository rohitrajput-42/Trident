from django.contrib import admin
from home.models import Post

class AdminPost(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']

admin.site.register(Post, AdminPost)