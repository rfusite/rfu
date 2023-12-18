from django.test import TestCase, Client
from django.urls import reverse
from cookie_consent.models import CookieGroup
from django.test import TestCase
from django.conf import settings
from unittest.mock import patch, MagicMock
from rfu.main_page.models import WebHero


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

    def create_mocked_webhero(self):
        # Создание мокированного объекта WebHero
        mocked_webhero = MagicMock()
        mocked_webhero.image_pattern1 = 'mocked_image.png'
        return mocked_webhero

    @patch('rfu.main_page.models.WebHero.objects.first')
    def test_index_view_cookie_data(self, mock_webhero):
        # Установка мокированного значения для WebHero.objects.first()
        mock_webhero.return_value = self.create_mocked_webhero()

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Group 1', response.content.decode())
        self.assertIn('Test Group 2', response.content.decode())

    @patch('rfu.main_page.models.WebHero.objects.first')
    def test_save_cookie_settings(self, mock_webhero):
        mock_webhero.return_value = self.create_mocked_webhero()

        # Тестирование сохранения настроек cookies
        response = self.client.post(reverse('save_cookie_settings'), {
            'testgroup1': 'on',
            'testgroup2': 'off',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.cookies['testgroup1'].value, 'True')
        self.assertEqual(self.client.cookies['testgroup2'].value, 'False')

    @patch('rfu.main_page.models.WebHero.objects.first')
    def test_cookie_settings(self, mock_webhero):
        mock_webhero.return_value = self.create_mocked_webhero()

        # Проверка настроек cookies
        self.client.post(reverse('save_cookie_settings'), {
            'testgroup1': 'on',
            'testgroup2': 'off',
        })
        testgroup1_cookie = self.client.cookies.get('testgroup1')
        testgroup2_cookie = self.client.cookies.get('testgroup2')

        self.assertIsNotNone(testgroup1_cookie)
        self.assertIsNotNone(testgroup2_cookie)
        self.assertEqual(testgroup1_cookie.value, 'True')
        self.assertEqual(testgroup2_cookie.value, 'False')


@patch('rfu.main_page.models.WebHero.objects.first', return_value=MagicMock(image_pattern1='mocked_image.png'))
class LanguageSwitchTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_default_language(self, mock_webhero):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Главная", response.content.decode())

    def check_language(self, lang_code, text, mock_webhero):
        self.client.cookies.load({settings.LANGUAGE_COOKIE_NAME: lang_code})
        response = self.client.get('/')
        self.assertIn(text, response.content.decode())

    def test_english_language(self, mock_webhero):
        self.check_language('en', "Home", mock_webhero)

    def test_russian_language(self, mock_webhero):
        self.check_language('ru', "Главная", mock_webhero)

    def test_ukrainian_language(self, mock_webhero):
        self.check_language('ua', "Головна", mock_webhero)

    def test_polish_language(self, mock_webhero):
        self.check_language('pl', "Główna", mock_webhero)
