from django.urls import reverse
from django.views.generic import TemplateView
from rfu.main_page.models import (Mission, OurWork, ModalWindow,
                                  PaymentMethod, SocialNetwork,
                                  Crypto, CookiesConsent,
                                  WebHero, HelpUs)
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect, HttpResponseForbidden
import rollbar
from django.core.exceptions import PermissionDenied
from django.middleware.csrf import CsrfViewMiddleware
import logging

logger = logging.getLogger(__name__)


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        try:
            context = super().get_context_data(**kwargs)
            context['webhero'] = WebHero.objects.first()
            context['modal_windows'] = ModalWindow.objects.all().order_by('id')
            context['missions'] = Mission.objects.all().order_by('id')
            context['our_works'] = OurWork.objects.all().order_by('id')
            context['help_us'] = HelpUs.objects.all().order_by('id')
            context['payment_methods'] = PaymentMethod.objects.all().order_by('id')
            context['crypto'] = Crypto.objects.all()
            context['social_networks'] = SocialNetwork.objects.all()
            context['cookies_consent'] = CookiesConsent.objects.first()
            return context

        except Exception as e:
            rollbar.report_exc_info()
            raise e


class GDPRView(TemplateView):
    template_name = 'GDPR.html'


class CookiePolicyView(TemplateView):
    template_name = 'cookie_policy.html'


def manage_cookies(request):
    """
    Простое управление cookies без сторонних пакетов
    """
    # Определяем типы cookies и их текущее состояние
    cookie_types = [
        {
            'name': 'analytics_cookies',
            'label': 'Аналитические cookies',
            'description': 'Помогают нам понимать, как посетители используют сайт',
            'is_checked': request.COOKIES.get('analytics_cookies', 'false') == 'true',
            'required': False,
        },
        {
            'name': 'marketing_cookies',
            'label': 'Маркетинговые cookies',
            'description': 'Используются для показа релевантной рекламы',
            'is_checked': request.COOKIES.get('marketing_cookies', 'false') == 'true',
            'required': False,
        },
        {
            'name': 'functional_cookies',
            'label': 'Функциональные cookies',
            'description': 'Обеспечивают дополнительную функциональность сайта',
            'is_checked': request.COOKIES.get('functional_cookies', 'false') == 'true',
            'required': False,
        }
    ]
    
    return render(request, 'cookie_consent/manage_bar.html', {
        'cookie_types': cookie_types
    })


@require_POST
def save_cookie_settings(request):
    """
    Простое сохранение настроек cookies
    """
    try:
        response = HttpResponseRedirect(reverse('index'))
        
        # Устанавливаем основной cookie согласия
        response.set_cookie('cookie_consent_accepted', 'true', max_age=365 * 24 * 60 * 60)
        
        if 'accept_all' in request.POST:
            # Принять все cookies
            response.set_cookie('analytics_cookies', 'true', max_age=365 * 24 * 60 * 60)
            response.set_cookie('marketing_cookies', 'true', max_age=365 * 24 * 60 * 60)
            response.set_cookie('functional_cookies', 'true', max_age=365 * 24 * 60 * 60)
            
        elif 'accept_necessary' in request.POST:
            # Принять только необходимые cookies
            response.set_cookie('analytics_cookies', 'false', max_age=365 * 24 * 60 * 60)
            response.set_cookie('marketing_cookies', 'false', max_age=365 * 24 * 60 * 60)
            response.set_cookie('functional_cookies', 'false', max_age=365 * 24 * 60 * 60)
            
        else:
            # Кастомные настройки от пользователя
            analytics = 'true' if request.POST.get('analytics_cookies') else 'false'
            marketing = 'true' if request.POST.get('marketing_cookies') else 'false'
            functional = 'true' if request.POST.get('functional_cookies') else 'false'
            
            response.set_cookie('analytics_cookies', analytics, max_age=365 * 24 * 60 * 60)
            response.set_cookie('marketing_cookies', marketing, max_age=365 * 24 * 60 * 60)
            response.set_cookie('functional_cookies', functional, max_age=365 * 24 * 60 * 60)
        
        return response
        
    except Exception as e:
        logger.error(f"Error saving cookie settings: {e}")
        return HttpResponseRedirect(reverse('index'))
