from django.db import models


class WebHero(models.Model):
    image = models.ImageField(upload_to='web_hero/', default='https://via.placeholder.com/2400x800')


class Mission(models.Model):
    header = models.CharField(max_length=255)
    text = models.TextField()


class Card(models.Model):
    image = models.ImageField(upload_to='cards/', default='https://via.placeholder.com/400')
    title = models.CharField(max_length=100)
    description = models.TextField()
    button = models.URLField(blank=True, null=True)


class PaymentMethod(models.Model):
    ICON_CHOICES = [
        ('bi-wallet2', 'Wallet'),
        ('bi-paypal', 'Paypal'),
        ('bi-heart', 'GoFundMe'),
        ('bi-currency-bitcoin', 'Bitcoin'),
        ('bi-currency-ethereum', 'ETH'),
        ('bi-cash', 'USDT (TRC20)'),
    ]
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True, null=True)  # Текстовое описание
    link = models.URLField(blank=True, null=True)  # Фактическая ссылка


class SocialNetwork(models.Model):
    ICON_CHOICES = [
        ('bi-facebook', 'Facebook'),
        ('bi-twitter', 'Twitter'),
        ('bi-telegram', 'Telegram'),
    ]
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, blank=True, null=True)
    name = models.CharField(max_length=200)
    link = models.URLField()


class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/', default='https://via.placeholder.com/100')
    url = models.URLField()


class Footer(models.Model):
    address = models.TextField()
    legal_links = models.TextField()
