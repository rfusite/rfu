from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Mission, Card,
                     PaymentMethod, SocialNetwork,
                     Partner, Footer, TranslatedText, Crypto)


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['get_header', 'get_text']
    search_fields = ['header', 'text']
    empty_value_display = '-пусто-'

    def get_header(self, obj):
        return obj.get_header()
    get_header.short_description = 'Header'

    def get_text(self, obj):
        return obj.get_text()
    get_text.short_description = 'Text'


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['get_title', 'get_description', 'button']
    list_display_links = ['get_title']
    search_fields = ['title', 'description']
    empty_value_display = '-пусто-'
    list_filter = ['title', 'description']

    def get_title(self, obj):
        return obj.get_title()
    get_title.short_description = 'Title'

    def get_description(self, obj):
        return obj.get_description()
    get_description.short_description = 'Description'

    def image_display(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" height="50" />')
        return "No Image"
    image_display.short_description = 'Image'


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'description', 'link']
    list_display_links = ['name']
    search_fields = ['name']
    empty_value_display = '-пусто-'
    list_filter = ['icon']
    list_editable = ['description']


@admin.register(Crypto)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'description', 'link']
    list_display_links = ['name']
    search_fields = ['name']
    empty_value_display = '-пусто-'
    list_filter = ['icon']
    list_editable = ['description']


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'link']
    list_display_links = ['name']
    search_fields = ['name']
    empty_value_display = '-пусто-'
    list_filter = ['icon']


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ['logo', 'url']
    search_fields = ['url']
    empty_value_display = '-пусто-'


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['get_address', 'get_legal_links']
    search_fields = ['address_text_id', 'legal_links_text_id']
    empty_value_display = '-пусто-'

    def get_address(self, obj):
        return obj.get_address()
    get_address.short_description = 'Address'

    def get_legal_links(self, obj):
        return obj.get_legal_links()
    get_legal_links.short_description = 'Legal Links'


@admin.register(TranslatedText)
class TranslatedTextAdmin(admin.ModelAdmin):
    list_display = ['text_id', 'language', 'text']
    list_display_links = ['text_id']
    list_filter = ['language']
    search_fields = ['text_id', 'text']
    list_editable = ['language', 'text']
