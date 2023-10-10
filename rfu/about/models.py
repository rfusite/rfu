from django.db import models


class PressRelease(models.Model):
    media_name = models.CharField(max_length=255)
    header = models.CharField(max_length=255)
    link = models.URLField()
    date = models.DateField()
