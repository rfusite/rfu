from django.shortcuts import render
from .models import PressRelease


def about(request):
    articles = PressRelease.objects.all()
    return render(request, 'about.html', {'articles': articles})
