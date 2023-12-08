from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from .models import RichTextFlatPage
from django.db import models
from ckeditor.widgets import CKEditorWidget


class RichTextFlatPageAdmin(FlatPageAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget()}
    }
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('enable_comments', 'registration_required', 'template_name'),
        }),
    )


admin.site.unregister(FlatPage)
admin.site.register(RichTextFlatPage, RichTextFlatPageAdmin)
