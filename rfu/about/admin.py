from django.contrib import admin
from .models import PressRelease


@admin.register(PressRelease)
class PressReleaseAdmin(admin.ModelAdmin):
    list_display = ['media_name', 'header', 'date']
    list_display_links = ['header']
    search_fields = ['media_name', 'header']
    empty_value_display = '-пусто-'
    list_filter = ['date']
    list_editable = ['date']
