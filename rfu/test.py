from django.test import TestCase, Client
from django.urls import reverse
from cookie_consent.models import CookieGroup
from django.test import TestCase
from django.conf import settings

# class CookieConsentTests(TestCase):
#     def setUp(self):
#         self.client = Client()
#
#     def test_essential_cookies_set(self):
#         response = self.client.get(reverse('index'))
#         self.assertIn('sessionid', response.cookies)
#         self.assertIn('csrftoken', response.cookies)
#
#     def test_functionality_cookies_set_with_consent(self):
#         # Simulate giving consent for functionality cookies
#         self.client.post(reverse('set_cookie_consent'), {'functionality': 'accepted'})
#         response = self.client.get(reverse('index'))
#         self.assertIn('django_language', response.cookies)
#
#     def test_performance_cookies_not_set_without_consent(self):
#         response = self.client.get(reverse('index'))
#         self.assertNotIn('_ga', response.cookies)
#         self.assertNotIn('_gid', response.cookies)
#         self.assertNotIn('_gat', response.cookies)
#
#     # Add more tests for other scenarios


class CookieManagementTest(TestCase):
    def setUp(self):
        # Создание тестовых данных для групп cookies
        self.cookie_group1 = CookieGroup.objects.create(name='Test Group 1', varname='testgroup1')
        self.cookie_group2 = CookieGroup.objects.create(name='Test Group 2', varname='testgroup2')
        self.client = Client()

    def test_index_view_cookie_data(self):
        # Тестирование того, что главная страница отображает данные о cookies
        response = self.client.get(reverse('index'))  # Используйте название маршрута, если оно есть
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Group 1', response.content.decode())
        self.assertIn('Test Group 2', response.content.decode())

    def test_save_cookie_settings(self):
        # Тестирование сохранения настроек cookies
        response = self.client.post(reverse('save_cookie_settings'), {
            'testgroup1': 'on',
            'testgroup2': 'off',
        })
        self.assertEqual(response.status_code, 302)  # Проверяем редирект
        self.assertEqual(self.client.cookies['testgroup1'].value, 'True')  # Проверяем, что cookie установлен
        self.assertEqual(self.client.cookies['testgroup2'].value, 'False')  # Проверяем, что cookie установлен

    def test_cookie_settings(self):
        # Предположим, что пользователь выбрал активацию 'testgroup1' и деактивацию 'testgroup2'
        self.client.post(reverse('save_cookie_settings'), {
            'testgroup1': 'on',
            'testgroup2': 'off',
        })

        # Проверяем, что cookies установлены с правильными значениями
        testgroup1_cookie = self.client.cookies.get('testgroup1')
        testgroup2_cookie = self.client.cookies.get('testgroup2')

        self.assertIsNotNone(testgroup1_cookie)
        self.assertIsNotNone(testgroup2_cookie)
        self.assertEqual(testgroup1_cookie.value, 'True')
        self.assertEqual(testgroup2_cookie.value, 'False')


class LanguageSwitchTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_default_language(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Проверка текста на языке по умолчанию (предположим, что это английский)
        self.assertIn("Главная", response.content.decode())

    def check_language(self, lang_code, text):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: lang_code})
        response = self.client.get('/')
        self.assertIn(text, response.content.decode())

    def test_english_language(self):
        self.check_language('en', "Home")

    def test_russian_language(self):
        self.check_language('ru', "Главная")

    def test_ukrainian_language(self):
        self.check_language('ua', "Головна")

    def test_polish_language(self):
        self.check_language('pl', "Główna")
