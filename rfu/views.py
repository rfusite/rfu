from django.urls import reverse
from django.views.generic import TemplateView
from rfu.main_page.models import (Mission, OurWork, ModalWindow,
                                  PaymentMethod, SocialNetwork,
                                  Crypto, CookiesConsent,
                                  WebHero, HelpUs)
from django.shortcuts import render
from cookie_consent.models import CookieGroup
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
            context['cookie_groups'] = CookieGroup.objects.all()
            return context

        except Exception as e:
            rollbar.report_exc_info()
            raise e


class GDPRView(TemplateView):
    template_name = 'GDPR.html'


class CookiePolicyView(TemplateView):
    template_name = 'cookie_policy.html'


def manage_cookies(request):
    # Список для хранения информации о группах и их состоянии
    cookie_info = []
    for group in CookieGroup.objects.all():
        cookie_info.append({
            'varname': group.varname,
            'name': group.name,
            'description': group.description,
            'is_checked': request.COOKIES.get(group.varname, 'False') == 'True',
            'is_deletable': group.is_deletable,
        })
    return render(request, 'cookie_consent/manage_bar.html', {'cookie_info': cookie_info})


@require_POST
def save_cookie_settings(request):
    try:
        response = HttpResponseRedirect(reverse('index'))

        # Получаем объекты всех групп кук
        cookie_groups = CookieGroup.objects.all()

        # Создаём словарь для хранения состояния согласия
        consent_dict = {
            group.varname: 'False'  # Устанавливаем начальное значение 'False'
            for group in cookie_groups
        }

        if 'accept_all' in request.POST:
            # Если приняты все куки, устанавливаем каждую группу в 'True'
            consent_dict.update({group.varname: 'True' for group in cookie_groups})
        elif 'accept_necessary' in request.POST:
            # Если приняты только необходимые куки
            for group in cookie_groups:
                consent_dict[group.varname] = 'True' if not group.is_deletable else 'False'
        else:
            # Если пользователь устанавливает кастомные настройки
            for group in cookie_groups:
                # Для неизменяемых кук устанавливаем значение True
                if not group.is_deletable:
                    consent_dict[group.varname] = 'True'
                else:
                    consent_given = request.POST.get(group.varname) == 'on'
                    consent_dict[group.varname] = 'True' if consent_given else 'False'

        # Устанавливаем куки согласно словарю согласия
        for varname, value in consent_dict.items():
            response.set_cookie(varname, value, max_age=365 * 24 * 60 * 60)

        # Создание строки для куки 'cookie_consent'
        consent_values = "|".join([f"{varname}={value}" for varname, value in consent_dict.items()])
        response.set_cookie('cookie_consent', consent_values, max_age=365 * 24 * 60 * 60)

        return response

    except PermissionDenied as e:
        if isinstance(e, CsrfViewMiddleware):
            logger.error("CSRF token mismatch encountered.")
            # Также можно добавить дополнительные детали в лог, если требуется
        return HttpResponseForbidden("Ошибка CSRF: Несоответствие токена")
