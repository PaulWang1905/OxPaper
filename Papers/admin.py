from django.contrib import admin

# Register your models here.

from .models import Page, Post, Category

admin.site.register(Page)
admin.site.register(Post)
admin.site.register(Category)

