from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug']
    search_fields = ['title', 'content']
    readonly_fields = ['created_at', 'updated_at']

admin.site.register(Article, ArticleAdmin)