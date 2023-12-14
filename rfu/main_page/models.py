from django.db import models
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _


class WebHero(models.Model):
    cars_count = models.CharField(max_length=50, verbose_name=_("Машин"), blank=True, null=True, default=350)
    volunteers_count = models.IntegerField(verbose_name=_("Волонтеров"), blank=True, null=True, default=320)
    shelter_refugees_count = models.CharField(max_length=50,
                                              verbose_name=_("Беженцев в шелтере"),
                                              blank=True,
                                              null=True,
                                              default="2600")
    days_of_war = models.IntegerField(verbose_name=_("Дней войны"), blank=True, null=True)
    days_of_rfu = models.IntegerField(verbose_name=_("Дней RFU"), blank=True, null=True)
    humanitarian_goods_weight = models.CharField(max_length=50,
                                                 verbose_name=_("Гуманитарных грузов"),
                                                 blank=True,
                                                 null=True,
                                                 default=50)
    flights_count = models.IntegerField(verbose_name=_("Рейсы"), blank=True, null=True, default=92)

    def save(self, *args, **kwargs):
        if not self.pk and WebHero.objects.exists():
            # если объект уже существует, не создавать новый
            return
        return super(WebHero, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Web Hero")
        verbose_name_plural = _("Web Heroes")


class Mission(models.Model):
    header = models.ForeignKey('TranslatedText',
                               on_delete=models.CASCADE,
                               related_name='mission_header',
                               blank=True,
                               null=True)
    text = models.ForeignKey('TranslatedText',
                             on_delete=models.CASCADE,
                             related_name='mission_text',
                             blank=True,
                             null=True)

    def __str__(self):
        return self.get_header()

    def get_header(self):
        if self.header:
            return self.header.text
        return "No translation available"

    def get_text(self):
        if self.text:
            return self.text.text
        return "No translation available"


class Card(models.Model):
    image = models.ImageField(upload_to='cards/', default='https://via.placeholder.com/400')
    title = models.ForeignKey('TranslatedText',
                              on_delete=models.CASCADE,
                              related_name='card_title',
                              blank=True, null=True)
    description = models.ForeignKey('TranslatedText',
                                    on_delete=models.CASCADE,
                                    related_name='card_description',
                                    blank=True,
                                    null=True)
    button = models.URLField(blank=True, null=True)

    def get_title(self):
        if self.title:
            return self.title.text
        return "No translation available"

    def get_description(self):
        if self.description:
            return self.description.text
        return "No translation available"

    @staticmethod
    def get_text(text_id):
        language = get_language() or 'en'
        try:
            return TranslatedText.objects.get(text_id=text_id, language=language).text
        except TranslatedText.DoesNotExist:
            return "No translation available"


class PaymentMethod(models.Model):
    ICONS = [
        ('bi-wallet2', 'Wallet'),
        ('bi-paypal', 'Paypal'),
        ('bi-heart', 'GoFundMe'),
    ]
    icon = models.CharField(max_length=50, choices=ICONS, blank=True, null=True)
    image = models.CharField(max_length=255, default='https://via.placeholder.com/150x50', blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    link = models.URLField(blank=True, null=True)


class Crypto(models.Model):
    ICONS = [
        ('bi-currency-bitcoin', 'Bitcoin'),
        ('bi-currency-ethereum', 'ETH'),
        ('bi-cash', 'USDT (TRC20)'),
    ]
    icon = models.CharField(max_length=50, choices=ICONS, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)
    link = models.URLField(blank=True, null=True)


class SocialNetwork(models.Model):
    ICONS = [
        ('bi-facebook', 'Facebook'),
        ('bi-twitter', 'Twitter'),
        ('bi-telegram', 'Telegram'),
    ]
    icon = models.CharField(max_length=50, choices=ICONS, blank=True, null=True)
    name = models.CharField(max_length=200)
    link = models.URLField()


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/', default='https://via.placeholder.com/100')
    url = models.URLField()


class Footer(models.Model):
    address = models.TextField()
    legal_links = models.TextField()


class TranslatedText(models.Model):
    LANGUAGES = [
        ('en', 'English'),
        ('ru', 'Russian'),
        ('uk', 'Ukrainian'),
        ('pl', 'Polish'),
    ]
    text_id = models.CharField(max_length=100, unique=True)
    language = models.CharField(max_length=10, choices=LANGUAGES, default='ru')
    text = models.TextField()

    def __str__(self):
        return f'{self.text_id} - {self.language}'

    class Meta:
        unique_together = (('text_id', 'language'),)
