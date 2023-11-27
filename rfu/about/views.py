import random
from django.shortcuts import render
from .models import PressRelease


def about(request):
    articles = PressRelease.objects.all()
    for article in articles:
        article.css_class = random.choice(['media-card-blue', 'media-card-yellow', 'media-card-white'])

    pattern_count = 9  # У вас есть 9 различных картинок
    articles_with_images = []

    for i, article in enumerate(articles, start=1):
        articles_with_images.append(article)
        if i % random.randint(3, 5) == 0:  # Вставка после каждой 3-й, 4-й или 5-й статьи
            pattern_number = random.randint(1, pattern_count)
            articles_with_images.append({
                'is_pattern': True,
                'pattern_number': pattern_number
            })

    return render(request, 'about.html',{'articles_with_images': articles_with_images})
