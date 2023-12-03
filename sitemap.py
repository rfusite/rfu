from django.contrib.sitemaps import Sitemap
from rfu.about.models import PressRelease
from rfu.blog.models import BlogPost, BlogImage
from rfu.main_page.models import WebHero, Mission, Card


class PressReleaseSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return PressRelease.objects.all()


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()


class BlogImageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return BlogImage.objects.all()


class WebHeroSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return WebHero.objects.all()


class MissionSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Mission.objects.all()


class CardSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Card.objects.all()
