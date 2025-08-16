from django import forms
from django.conf import settings
from django.contrib import admin
from django.db.models.fields import CharField, TextField
from django.utils.html import format_html
from modeltranslation.translator import translator
from openai import OpenAI

from rfu.main_page.models import (
    Mission, OurWork, HelpUs, ModalWindow, PaymentMethod, SocialNetwork,
    Footer, Crypto, WebHero, CookiesConsent
)
from .widgets import ImagePatternSelect

import logging

def translate_model(modeladmin, request, queryset):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
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

                        response = client.completions.create(
                            model="gpt-3.5-turbo-instruct",
                            prompt=f"Please translate this to {lang_name}: {source_value}",
                            temperature=0.5,
                            max_tokens=500
                        )
                        translated_text = response.choices[0].text.strip()
                        translated_field_name = f'{field_name}_{lang_code}'
                        setattr(obj, translated_field_name, translated_text)

        obj.save()

def has_image_and_alt_text_fields(obj):
    return hasattr(obj, 'image') and hasattr(obj, 'image_alt_text')

def generate_alt_text(modeladmin, request, queryset):
    logger = logging.getLogger('django')
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    base_url = "https://rfu2022.org"

    for obj in queryset:
        if has_image_and_alt_text_fields(obj):
            full_image_url = base_url + obj.image.url
            logger.info(f"Full image URL: {full_image_url}")
            response = client.chat.completions.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Provide a concise alt text for the image. Avoid translating text in the image."},
                            {"type": "image_url", "image_url": full_image_url}
                        ]
                    }
                ]
            )

            alt_text_ru = response.choices[0].message.content if response.choices else "Alt text not generated"
            obj.image_alt_text = alt_text_ru
            translate_alt_text(obj, alt_text_ru)
            obj.save()

def translate_alt_text(obj, source_text):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    for lang_code, lang_name in settings.LANGUAGES:
        if lang_code == 'ru':
            continue

        response = client.completions.create(
            model="gpt-3.5-turbo-instruct",
            prompt=f"Please translate this to {lang_name}: {source_text}",
            temperature=0.5,
            max_tokens=500
        )
        translated_text = response.choices[0].text.strip()
        translated_field_name = f'image_alt_text_{lang_code}'
        if hasattr(obj, translated_field_name):
            setattr(obj, translated_field_name, translated_text)

generate_alt_text.short_description = "Generate Alt Text for Images"

class WebHeroAdminForm(forms.ModelForm):
    class Meta:
        model = WebHero
        fields = '__all__'
        widgets = {
            'image_pattern1': ImagePatternSelect(),
            'image_pattern2': ImagePatternSelect(),
            'image_pattern3': ImagePatternSelect(),
        }

class WebHeroAdmin(admin.ModelAdmin):
    form = WebHeroAdminForm
    list_display = (
        'h1_title',
        'image_pattern1',
        'image_pattern2',
        'image_pattern3',
        'cars_count',
        'volunteers_count',
        'shelter_refugees_count',
        'get_days_of_war',
        'get_days_of_rfu',
        'humanitarian_goods_weight',
        'flights_count',
        'cars_count_label',
        'volunteers_count_label',
        'shelter_refugees_count_label',
        'days_of_war_label',
        'days_of_rfu_label',
        'humanitarian_goods_weight_label',
        'flights_count_label'
    )
    search_fields = (
        'h1_title',
        'cars_count',
        'volunteers_count',
        'shelter_refugees_count'
    )
    list_filter = (
        'cars_count',
        'volunteers_count',
        'shelter_refugees_count'
    )
    readonly_fields = [
        'get_days_of_war',
        'get_days_of_rfu',
        'image_pattern1_preview',
        'image_pattern2_preview',
        'image_pattern3_preview'
    ]

    def image_pattern1_preview(self, obj):
        return self._image_preview(obj.image_pattern1)

    def image_pattern2_preview(self, obj):
        return self._image_preview(obj.image_pattern2)

    def image_pattern3_preview(self, obj):
        return self._image_preview(obj.image_pattern3)

    def _image_preview(self, image_pattern):
        if image_pattern:
            return format_html('<img src="/static/pattern/{}" style="max-height: 100px;"/>', image_pattern)
        return ""

    fieldsets = (
        ('H1 Title Translations', {
            'fields': (
                ('h1_title_ru',
                 'h1_title_en',
                 'h1_title_de',
                 'h1_title_ua',
                 'h1_title_pl'),
            ),
        }),
        ('Image Patterns', {
            'fields': (
                ('image_pattern1', 'image_pattern1_preview'),
                ('image_pattern2', 'image_pattern2_preview'),
                ('image_pattern3', 'image_pattern3_preview')
            )
        }),
        ('Counters', {
            'fields': (
                'cars_count',
                'volunteers_count',
                'shelter_refugees_count',
                'humanitarian_goods_weight',
                'flights_count'
            ),
        }),
        ('Counter Labels Translations', {
            'fields': (
                ('cars_count_label_en',
                 'cars_count_label_de',
                 'cars_count_label_ru',
                 'cars_count_label_ua',
                 'cars_count_label_pl'),
                ('volunteers_count_label_en',
                 'volunteers_count_label_de',
                 'volunteers_count_label_ru',
                 'volunteers_count_label_ua',
                 'volunteers_count_label_pl'),
                ('shelter_refugees_count_label_en',
                 'shelter_refugees_count_label_de',
                 'shelter_refugees_count_label_ru',
                 'shelter_refugees_count_label_ua',
                 'shelter_refugees_count_label_pl'),
                ('humanitarian_goods_weight_label_en',
                 'humanitarian_goods_weight_label_de',
                 'humanitarian_goods_weight_label_ru',
                 'humanitarian_goods_weight_label_ua',
                 'humanitarian_goods_weight_label_pl'),
                ('flights_count_label_en',
                 'flights_count_label_de',
                 'flights_count_label_ru',
                 'flights_count_label_ua',
                 'flights_count_label_pl')
            ),
        }),
        ('Dynamic Calculations', {
            'fields': (
                'get_days_of_war',
                'get_days_of_rfu'
            ),
        }),
    )

admin.site.register(WebHero, WebHeroAdmin)
