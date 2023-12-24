from modeltranslation.translator import register, TranslationOptions
from .models import WebHero, Mission, OurWork, HelpUs, ModalWindow, CookiesConsent, PaymentMethod


@register(WebHero)
class WebHeroTranslationOptions(TranslationOptions):
    fields = ('cars_count_label', 'volunteers_count_label', 'shelter_refugees_count_label', 'days_of_war_label',
              'days_of_rfu_label', 'humanitarian_goods_weight_label', 'flights_count_label', 'h1_title')


@register(ModalWindow)
class ModalWindowTranslationOptions(TranslationOptions):
    fields = ('text', 'image_alt_text')


@register(Mission)
class MissionTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'image_alt_text')


@register(OurWork)
class OurWorkTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'image_alt_text')


@register(HelpUs)
class HelpUsTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'image_alt_text')


@register(PaymentMethod)
class PaymentMethodTranslationOptions(TranslationOptions):
    fields = ('image_alt_text',)


@register(CookiesConsent)
class CookiesConsentTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'essential_text', 'functional_text', 'analytics_text', 'marketing_text')
