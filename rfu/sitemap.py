from django.contrib.sitemaps import Sitemap
from django.contrib.flatpages.models import FlatPage
from django.urls import reverse
from math import ceil
from rfu.media.models import PressRelease
from rfu.blog.models import BlogPost


class StaticViewSitemap(Sitemap):
    priority = 0.6
    changefreq = 'monthly'

    def items(self):
        # Возвращает список имен URL-адресов статических страниц
        return ['index', 'media', 'blog']  # Замените на ваши URL-имена

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        # Возвращает список номеров страниц для пагинации
        posts_per_page = 4
        total_posts = BlogPost.objects.count()
        total_pages = ceil(total_posts / posts_per_page)
        return range(1, total_pages + 1)

    def location(self, page_number):
        if page_number == 1:
            return reverse('blog')  # URL первой страницы блога
        else:
            return reverse('blog') + f'?page={page_number}'  # URL для пагинированных страниц


class MediaSiteMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        # Возвращает список номеров страниц для пагинации
        posts_per_page = 12
        total_posts = PressRelease.objects.count()
        total_pages = ceil(total_posts / posts_per_page)
        return range(1, total_pages + 1)

    def location(self, page_number):
        if page_number == 1:
            return reverse('media')  # URL первой страницы раздела "about"
        else:
            return reverse('media') + f'?page={page_number}'  # URL для пагинированных страниц


class FlatPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return FlatPage.objects.all()
