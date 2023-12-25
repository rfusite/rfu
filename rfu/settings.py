"""
Django settings for rfu project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path
import dj_database_url
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG') == 'True'
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

ALLOWED_HOSTS = ['rfu2022.org',
                 'www.rfu2022.org',
                 'rfu-production.up.railway.app',
                 '127.0.0.1',
                 'localhost',]

# Application definition
INSTALLED_APPS = [
    # Other apps
    'bootstrap4',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'cookie_consent',
    'ckeditor',
    'ckeditor_uploader',
    'debug_toolbar',
    'dbbackup',
    'modeltranslation',

    # Your custom apps
    'rfu',
    "rfu.main_page",
    "rfu.blog",
    "rfu.media",
    "rfu.extended_flatpages",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cookie_consent.middleware.CleanCookiesMiddleware",
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'djangorescue.middleware.StaticMediaMiddleware',
    'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    # 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]


ROOT_URLCONF = "rfu.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                'django.template.context_processors.i18n',
                'rfu.context_processors.cookie_settings',
                'rfu.context_processors.footer_context',
            ],
        },
    },
]

# ROLLBAR = {
#     'access_token': os.getenv('ROLLBAR_ACCESS_TOKEN'),
#     'environment': 'development' if DEBUG else 'production',
#     'code_version': '1.0',
#     'root': BASE_DIR,
# }

WSGI_APPLICATION = "rfu.wsgi.application"

SITE_ID = 2
WAGTAIL_SITE_NAME = 'RFU'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator", },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator", },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator", },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator", },
]

CSRF_TRUSTED_ORIGINS = ['https://rfu-production.up.railway.app',
                        'https://rfu2022.org',
                        'https://www.rfu2022.org']


ROLLBAR = {
    'access_token': os.getenv('ROLLBAR_ACCESS_TOKEN'),
    'environment': 'development' if DEBUG else 'production',
    'code_version': '1.0',
    'root': BASE_DIR,
}


# settings.py

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'INFO',
#         },
#     },
# }




# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


LANGUAGE_CODE = "ru"

LANGUAGES = [
    ('en', 'English'),
    ('ru', 'Russian'),
    ('ua', 'Ukrainian'),
    ('pl', 'Polish'),
    ('de', 'German'),
]


TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/uploads/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Настройки django-dbbackup
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = dict(location=BASE_DIR / 'backups')
DBBACKUP_STORAGE_OPTIONS['encryption'] = True

MODELTRANSLATION_TRANSLATION_REGISTRY = "rfu.main_page.translation"

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
