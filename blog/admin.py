from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Tag, Post, Page


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Page)