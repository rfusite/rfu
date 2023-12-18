from django.db import models


class PressRelease(models.Model):
    media_name = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    link = models.URLField(max_length=300)
    date = models.DateField()
