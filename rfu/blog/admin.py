from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'likes']
    list_display_links = ['title']
    search_fields = ['title', 'content']
    empty_value_display = '-пусто-'
    list_filter = ['created_at']
    list_editable = ['likes']
