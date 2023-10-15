from django.views.generic import TemplateView
from rfu.main_page.models import WebHero, Mission, Card, PaymentMethod, SocialNetwork, Partner, Footer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Добавляем все объекты каждой модели в контекст
        context['web_hero'] = WebHero.objects.first()
        context['missions'] = Mission.objects.all()
        context['cards'] = Card.objects.all()
        context['payment_methods'] = PaymentMethod.objects.all()
        context['social_networks'] = SocialNetwork.objects.all()
        context['partners'] = Partner.objects.all()
        context['footer'] = Footer.objects.all()

        return context
