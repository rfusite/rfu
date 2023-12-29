from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import PressRelease
import random


def media(request):
    articles = PressRelease.objects.all().order_by('-date')
    for article in articles:
        article.css_class = random.choice(['media-card-light-blue',
                                           'media-card-yellow',
                                           'media-card-white'])

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
    page = request.GET.get('page') or 1  # Значение по умолчанию для 'page' - 1

    try:
        page = int(page)  # Преобразуем page в целое число
        articles_with_images = paginator.page(page)
    except (PageNotAnInteger, ValueError, EmptyPage):
        # Если страница не является целым числом или выходит за пределы диапазона,
        # отображаем первую страницу
        articles_with_images = paginator.page(1)

    return render(request, 'smi/smi.html', {'articles_with_images': articles_with_images})
