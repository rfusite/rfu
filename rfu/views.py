from django.views.generic import TemplateView
from django.utils.timezone import now
from rfu.main_page.models import Mission, Card, PaymentMethod, SocialNetwork, Partner, Footer, Crypto
from datetime import date
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
        return context


class GDPRView(TemplateView):
    template_name = 'GDPR.html'


@csrf_exempt
def accept_cookies(request):
    if request.method == 'POST':
        response = JsonResponse({"message": "Согласие на использование файлов cookie сохранено"})
        response.set_cookie('user_cookie_consent', 'accepted', max_age=3600*24*365)
        return response


@csrf_exempt
def decline_cookies(request):
    if request.method == 'POST':
        response = JsonResponse({"message": "Отказ от использования файлов cookie сохранен"})
        response.set_cookie('user_cookie_consent', 'declined', max_age=3600*24*365)
        return response
