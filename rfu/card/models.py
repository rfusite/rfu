from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    description = models.TextField()
