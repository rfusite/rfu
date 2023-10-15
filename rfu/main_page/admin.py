from django.contrib import admin
from .models import WebHero, Mission, Card, PaymentMethod, SocialNetwork, Partner, Footer


@admin.register(WebHero)
class WebHeroAdmin(admin.ModelAdmin):
    list_display = ['image']
    search_fields = ['image']
    empty_value_display = '-пусто-'


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    list_display = ['header', 'text']
    search_fields = ['header']
    empty_value_display = '-пусто-'


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'button']
    list_display_links = ['title']
    search_fields = ['title']
    empty_value_display = '-пусто-'
    list_filter = ['title']


@admin.register(PaymentMethod)
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
    list_display = ['address', 'legal_links']
    search_fields = ['address']
    empty_value_display = '-пусто-'
