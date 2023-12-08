from django.urls import reverse
from django.views.generic import TemplateView
from django.utils.timezone import now
from rfu.main_page.models import Mission, Card, PaymentMethod, SocialNetwork, Partner, Footer, Crypto
from datetime import date
from django.shortcuts import render
from cookie_consent.models import CookieGroup
from django.views.decorators.http import require_POST
from django.http import HttpResponseRedirect


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_counters(self):
        days_of_war = (now().date() - date(2022, 2, 24)).days
        days_of_rfu = (now().date() - date(2022, 2, 26)).days
        return {
            'cars_count': 350,
            'volunteers_count': 320,
            'shelter_refugees_count': 2600,
            'days_of_war': days_of_war,
            'days_of_rfu': days_of_rfu,
            'humanitarian_goods_weight': '50 тонн',
            'flights_count': 92
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.get_counters())
        context['missions'] = Mission.objects.all()
        context['cards'] = Card.objects.all()
        context['payment_methods'] = PaymentMethod.objects.all()
        context['crypto'] = Crypto.objects.all()
        context['social_networks'] = SocialNetwork.objects.all()
        context['partners'] = Partner.objects.all()
        context['footer'] = Footer.objects.all()
        context['cookie_groups']  = CookieGroup.objects.all()
        # Ensure cookie_groups is a QuerySet or list of CookieGroup objects

        return context


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
    response = HttpResponseRedirect(reverse('index'))

    # Проверяем, какая кнопка была нажата
    if 'accept_all' in request.POST:
        # Устанавливаем все куки
        for group in CookieGroup.objects.all():
            response.set_cookie(group.varname, 'True', max_age=365 * 24 * 60 * 60)
    elif 'accept_necessary' in request.POST:
        # Устанавливаем только необходимые куки
        for group in CookieGroup.objects.all():
            consent_given = 'True' if not group.is_deletable else 'False'
            response.set_cookie(group.varname, consent_given, max_age=365 * 24 * 60 * 60)
    else:
        # Сохраняем кастомные настройки из формы
        for group in CookieGroup.objects.all():
            consent_given = request.POST.get(group.varname) == 'on'
            response.set_cookie(group.varname, consent_given, max_age=365 * 24 * 60 * 60)

    # Создание строки для куки 'cookie_consent'
    consent_values = "|".join([f"{group.varname}={request.POST.get(group.varname, 'off')}" for group in CookieGroup.objects.all()])
    response.set_cookie('cookie_consent', consent_values, max_age=365 * 24 * 60 * 60)

    return response
