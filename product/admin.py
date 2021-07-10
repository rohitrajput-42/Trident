from django.contrib import admin
from django.db import models
from .models import Item

class AdminItem(admin.ModelAdmin):

    list_display = ['Name', 'Weight', 'Price', 'created_at', 'updated_at']

admin.site.register(Item, AdminItem)