import os
import openai
from modeltranslation.translator import translator
from django.conf import settings
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (Mission, OurWork, HelpUs, ModalWindow,
                     PaymentMethod, SocialNetwork,
                     Footer, Crypto, WebHero, CookiesConsent)
from .widgets import ImagePatternSelect
from django import forms
from django.utils.html import format_html
from django.db.models.fields import CharField, TextField

openai.api_key = settings.OPENAI_API_KEY

def translate_model(modeladmin, request, queryset):
    for obj in queryset:
        translation_opts = translator.get_options_for_model(obj.__class__)

        for field_name in translation_opts.fields.keys():
            field_object = obj._meta.get_field(field_name)

            if isinstance(field_object, (CharField, TextField)):
                source_value = getattr(obj, field_name, None)
                if source_value:
                    for lang_code, lang_name in settings.LANGUAGES:
                        if lang_code == settings.LANGUAGE_CODE:
                            continue

                        response = openai.Completion.create(
                            model="gpt-3.5-turbo-instruct",
                            prompt=f"Please translate this to {lang_name}: {source_value}",
                            temperature=0.5,
                            max_tokens=500,
                            top_p=1,
                            frequency_penalty=0,
                            presence_penalty=0
                        )
                        translated_text = response.choices[0].text.strip()
                        translated_field_name = f'{field_name}_{lang_code}'
                        setattr(obj, translated_field_name, translated_text)

        obj.save()

class WebHeroAdminForm(forms.ModelForm):
    class Meta:
        model = WebHero
        fields = '__all__'
        widgets = {
            'image_pattern1': ImagePatternSelect(),
            'image_pattern2': ImagePatternSelect(),
            'image_pattern3': ImagePatternSelect(),
        }

@admin.register(WebHero)
class WebHeroAdmin(admin.ModelAdmin):
    form = WebHeroAdminForm
    list_display = (
        'h1_title', 'image_pattern1', 'image_pattern2', 'image_pattern3',
        'cars_count', 'volunteers_count', 'shelter_refugees_count',
        'get_days_of_war', 'get_days_of_rfu', 'humanitarian_goods_weight',
        'flights_count', 'cars_count_label', 'volunteers_count_label',
        'shelter_refugees_count_label', 'days_of_war_label',
        'days_of_rfu_label', 'humanitarian_goods_weight_label',
        'flights_count_label'
    )
    search_fields = (
        'h1_title', 'cars_count', 'volunteers_count', 'shelter_refugees_count',
        'humanitarian_goods_weight', 'flights_count',
        'cars_count_label', 'volunteers_count_label',
        'shelter_refugees_count_label', 'humanitarian_goods_weight_label',
        'flights_count_label'
    )
    list_filter = (
        'cars_count', 'volunteers_count', 'shelter_refugees_count',
        'humanitarian_goods_weight', 'flights_count'
    )
    readonly_fields = ['get_days_of_war', 'get_days_of_rfu', 'image_pattern1_preview', 'image_pattern2_preview',
                       'image_pattern3_preview']

    # Методы для отображения превью изображений
    def image_pattern1_preview(self, obj):
        return self._image_preview(obj.image_pattern1)

    def image_pattern2_preview(self, obj):
        return self._image_preview(obj.image_pattern2)

    def image_pattern3_preview(self, obj):
        return self._image_preview(obj.image_pattern3)

    # Универсальный метод для создания HTML превью
    def _image_preview(self, image_pattern):
        if image_pattern:
            return format_html('<img src="/static/pattern/{}" style="max-height: 100px;"/>', image_pattern)
        return ""

    # Если вы хотите, чтобы изображения можно было редактировать в админке
    fieldsets = (
        ('H1 Title Translations', {
            'fields': (
                ('h1_title_ru', 'h1_title_en', 'h1_title_de', 'h1_title_ua', 'h1_title_pl',),
            ),
        }),
        (None, {
            'fields': (('image_pattern1', 'image_pattern1_preview'), ('image_pattern2', 'image_pattern2_preview'), ('image_pattern3', 'image_pattern3_preview'),)
        }),
        ('Counters', {
            'fields': (
                'cars_count', 'volunteers_count', 'shelter_refugees_count',
                'humanitarian_goods_weight', 'flights_count',
            ),
        }),
        ('Counter Labels Translations', {
            'fields': (
                ('cars_count_label_en', 'cars_count_label_de', 'cars_count_label_ru', 'cars_count_label_ua', 'cars_count_label_pl',),
                ('volunteers_count_label_en', 'volunteers_count_label_de', 'volunteers_count_label_ru', 'volunteers_count_label_ua', 'volunteers_count_label_pl',),
                ('shelter_refugees_count_label_en', 'shelter_refugees_count_label_de', 'shelter_refugees_count_label_ru', 'shelter_refugees_count_label_ua', 'shelter_refugees_count_label_pl',),
                ('humanitarian_goods_weight_label_en', 'humanitarian_goods_weight_label_de', 'humanitarian_goods_weight_label_ru', 'humanitarian_goods_weight_label_ua', 'humanitarian_goods_weight_label_pl',),
                ('flights_count_label_en', 'flights_count_label_de', 'flights_count_label_ru', 'flights_count_label_ua', 'flights_count_label_pl',),
            ),
        }),
        ('Dynamic Calculations', {
            'fields': (
                'get_days_of_war', 'get_days_of_rfu',
            ),
        }),
    )


@admin.register(ModalWindow)
class ModalWindowAdmin(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ['id', 'text']

    fieldsets = (
        (None, {
            'fields': ('image',)
        }),
        ('Base Info', {
            'fields': ('id', 'text',)
        }),
        ('Translations', {
            'fields': (
                ('text_en', 'text_de', 'text_ru', 'text_ua', 'text_pl'),
            ),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['text'].label = 'Original text'
        return form


@admin.register(Mission)
class MissionAdmin(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ['title', 'text']

    fieldsets = (
        (None, {
            'fields': ('image',)
        }),
        ('Base Info', {
            'fields': ('title', 'text',)
        }),
        ('Translations', {
            'fields': (
                ('title_en', 'title_de', 'title_ru', 'title_ua', 'title_pl'),
                ('text_en', 'text_de', 'text_ru', 'text_ua', 'text_pl'),
            ),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = 'Original title'
        form.base_fields['text'].label = 'Original text'
        return form

@admin.register(OurWork)
class OurWork(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ['title', 'text']

    fieldsets = (
        (None, {
            'fields': ('image',)
        }),
        ('Base Info', {
            'fields': ('title', 'text',)
        }),
        ('Translations', {
            'fields': (
                ('title_en', 'title_de', 'title_ru', 'title_ua', 'title_pl'),
                ('text_en', 'text_de', 'text_ru', 'text_ua', 'text_pl'),
            ),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = 'Original title'
        form.base_fields['text'].label = 'Original text'
        return form

@admin.register(HelpUs)
class HelpUsAdmin(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ['title', 'text']

    fieldsets = (
        (None, {
            'fields': ('image',)
        }),
        ('Base Info', {
            'fields': ('title', 'text',)
        }),
        ('Translations', {
            'fields': (
                ('title_en', 'title_de', 'title_ru', 'title_ua', 'title_pl'),
                ('text_en', 'text_de', 'text_ru', 'text_ua', 'text_pl'),
            ),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = 'Original title'
        form.base_fields['text'].label = 'Original text'
        return form

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

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email_part1', 'email_part2', 'privacy_policy_link']
    search_fields = ['name']

@admin.register(CookiesConsent)
class CookiesConsentAdmin(admin.ModelAdmin):
    actions = [translate_model]
    list_display = ['title', 'text', 'essential_text', 'functional_text', 'analytics_text', 'marketing_text']

    fieldsets = (
        ('Base Info', {
            'fields': ('title', 'text', 'essential_text', 'functional_text', 'analytics_text', 'marketing_text',)
        }),
        ('Translations', {
            'fields': (
                ('title_en', 'title_de', 'title_ru', 'title_ua', 'title_pl'),
                ('text_en', 'text_de', 'text_ru', 'text_ua', 'text_pl'),
                ('essential_text_en', 'essential_text_de', 'essential_text_ru', 'essential_text_ua', 'essential_text_pl'),
                ('functional_text_en', 'functional_text_de', 'functional_text_ru', 'functional_text_ua', 'functional_text_pl'),
                ('analytics_text_en', 'analytics_text_de', 'analytics_text_ru', 'analytics_text_ua', 'analytics_text_pl'),
                ('marketing_text_en', 'marketing_text_de', 'marketing_text_ru', 'marketing_text_ua', 'marketing_text_pl'),
            ),
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title'].label = 'Original title'
        form.base_fields['text'].label = 'Original text'
        form.base_fields['essential_text'].label = 'Original essential text'
        form.base_fields['functional_text'].label = 'Original functional text'
        form.base_fields['analytics_text'].label = 'Original analytics text'
        form.base_fields['marketing_text'].label = 'Original marketing text'
        return form

