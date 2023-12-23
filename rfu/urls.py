"""rfu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from rfu.sitemap import StaticViewSitemap, BlogSitemap, FlatPageSitemap, MediaSiteMap
from rfu.views import IndexView, manage_cookies, save_cookie_settings, CookiePolicyView
from django.conf import settings
from django.views.generic.base import RedirectView
from django.views.generic.base import TemplateView
from django.views.static import serve
from django.conf.urls.static import static

sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
    'about': MediaSiteMap,
    'flatpages': FlatPageSitemap,
}

urlpatterns = [
    path('verwaltung2023/kontrollraum/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('rfu.blog.urls')),
    path('about/', include('rfu.about.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('cookie_policy/', CookiePolicyView.as_view(), name='cookie_policy'),
    path('manage-cookies/', manage_cookies, name='manage_cookies'),
    path('save-cookie-settings/', save_cookie_settings, name='save_cookie_settings'),
    path("cookies/", include("cookie_consent.urls")),
    path('google1a7ec7e933d1c3cac.html',
         TemplateView.as_view(template_name='google_console/google1ca7ec933d1c3cac.html'),
         name='google-verification'),

    # маршрут для sitemap
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    # маршрут для robotx.txt
    path('robots.txt',
         TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # Редиректы для главной страницы
    path('pl/', RedirectView.as_view(url='/', permanent=True)),
    path('en/', RedirectView.as_view(url='/', permanent=True)),
    path('en/#howtohelpus', RedirectView.as_view(url='/', permanent=True)),

    # Редиректы для страницы "about"
    path('media/', RedirectView.as_view(pattern_name='about', permanent=True)),
    path('pl/media/', RedirectView.as_view(pattern_name='about', permanent=True)),
    path('en/media/', RedirectView.as_view(pattern_name='about', permanent=True)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
