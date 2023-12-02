from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import PressRelease
import random


def about(request):
    articles = PressRelease.objects.all()
    for article in articles:
        article.css_class = random.choice(['media-card-blue', 'media-card-yellow', 'media-card-white'])

    pattern_count = 9
    articles_with_patterns = []

    for i, article in enumerate(articles, start=1):
        articles_with_patterns.append(article)
        if i % random.randint(3, 5) == 0:
            pattern_number = random.randint(1, pattern_count)
            articles_with_patterns.append({
                'is_pattern': True,
                'pattern_number': pattern_number
            })

    # Настройка пагинации
    paginator = Paginator(articles_with_patterns, 12)  # 12 элементов на странице
    page = request.GET.get('page')

    try:
        articles_with_images = paginator.page(page)
    except PageNotAnInteger:
        articles_with_images = paginator.page(1)
    except EmptyPage:
        articles_with_images = paginator.page(paginator.num_pages)

    return render(request, 'about.html', {'articles_with_images': articles_with_images})
