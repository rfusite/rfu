from django.utils.translation import get_language
from django.utils.timezone import now
from datetime import date
from django.db import models
from ckeditor.fields import RichTextField


class SingletonModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass


class WebHero(models.Model):
    PATTERN_CHOICES = (
        ('pattern1.png', 'Pattern 1'),
        ('pattern2.png', 'Pattern 2'),
        ('pattern3.png', 'Pattern 3'),
        ('pattern4.png', 'Pattern 4'),
        ('pattern5.png', 'Pattern 5'),
        ('pattern6.png', 'Pattern 6'),
        ('pattern7.png', 'Pattern 7'),
        ('pattern8.png', 'Pattern 8'),
        ('pattern9.png', 'Pattern 9'),
    )

    # Счетчики
    cars_count = models.CharField(max_length=50, blank=True, null=True, default=350)
    volunteers_count = models.IntegerField(blank=True, null=True, default=320)
    shelter_refugees_count = models.CharField(max_length=50, blank=True, null=True, default="2600")
    days_of_war = models.IntegerField(blank=True, null=True)
    days_of_rfu = models.IntegerField(blank=True, null=True)
    humanitarian_goods_weight = models.CharField(max_length=50, blank=True, null=True, default=50)
    flights_count = models.IntegerField(blank=True, null=True, default=92)

    # Лейблы счетчиков
    cars_count_label = models.CharField(max_length=100, blank=True, null=True)
    volunteers_count_label = models.CharField(max_length=100, blank=True, null=True)
    shelter_refugees_count_label = models.CharField(max_length=100, blank=True, null=True)
    days_of_war_label = models.CharField(max_length=100, blank=True, null=True)
    days_of_rfu_label = models.CharField(max_length=100, blank=True, null=True)
    humanitarian_goods_weight_label = models.CharField(max_length=100, blank=True, null=True)
    flights_count_label = models.CharField(max_length=100, blank=True, null=True)

    # Поле для заголовка h1
    h1_title = models.TextField(max_length=200, blank=True, null=True)

    # Поля для изображений
    image_pattern1 = models.CharField(max_length=50, choices=PATTERN_CHOICES, default='pattern1.png', blank=True)
    image_pattern2 = models.CharField(max_length=50, choices=PATTERN_CHOICES, default='pattern1.png', blank=True)
    image_pattern3 = models.CharField(max_length=50, choices=PATTERN_CHOICES, default='pattern1.png', blank=True)

    def get_days_of_war(self):
        return (now().date() - date(2022, 2, 24)).days

    def get_days_of_rfu(self):
        return (now().date() - date(2022, 2, 26)).days

    # Используйте свойства, чтобы можно было обращаться к методам как к атрибутам
    @property
    def days_of_war(self):
        return self.get_days_of_war()

    @property
    def days_of_rfu(self):
        return self.get_days_of_rfu()


class ModalWindow(models.Model):
    id = models.IntegerField(primary_key=True)
    text = RichTextField()
    image = models.ImageField(upload_to='main_page/modal_window/', default='https://via.placeholder.com/400')
    image_alt_text = models.CharField(max_length=200, blank=True, null=True)


class Mission(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='main_page/mission/', default='https://via.placeholder.com/400')
    image_alt_text = models.CharField(max_length=200, blank=True, null=True)


class OurWork(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='main_page/our_work/', default='https://via.placeholder.com/400')
    image_alt_text = models.CharField(max_length=200, blank=True, null=True)


class HelpUs(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = models.TextField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='main_page/help_us/', default='https://via.placeholder.com/400')
    image_alt_text = models.CharField(max_length=200, blank=True, null=True)


class PaymentMethod(models.Model):
    ICONS = [
        ('bi-wallet2', 'Wallet'),
        ('bi-paypal', 'Paypal'),
        ('bi-heart', 'GoFundMe'),
    ]
    icon = models.CharField(max_length=50, choices=ICONS, blank=True, null=True)
    image = models.CharField(max_length=255, default='https://via.placeholder.com/150x50', blank=True, null=True)
    image_alt_text = models.CharField(max_length=200, blank=True, null=True)
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


class Footer(SingletonModel):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(max_length=500, blank=True, null=True)
    email_part1 = models.CharField(max_length=50, blank=True, null=True)
    email_part2 = models.CharField(max_length=50, blank=True, null=True)
    privacy_policy_link = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return "Footer Configuration"


class CookiesConsent(SingletonModel):
    title = models.CharField(max_length=100, blank=True, null=True)
    text = RichTextField()
    essential_text = models.CharField(max_length=300, blank=True, null=True)
    analytics_text = models.CharField(max_length=300, blank=True, null=True)
    marketing_text = models.CharField(max_length=300, blank=True, null=True)
    performance_text = models.CharField(max_length=300, blank=True, null=True)
    functional_text = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return "Cookies Consent Configuration"
