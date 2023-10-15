from django.shortcuts import render
from .forms import WebHeroForm, CardForm, PartnerForm, FooterForm
from .models import WebHero


def manage_page(request):
    web_hero = WebHero.objects.first()
    web_hero_form = WebHeroForm(instance=web_hero)
    card_form = CardForm()
    partner_form = PartnerForm()
    footer_form = FooterForm()

    return render(request, 'manage_page.html', {
        'web_hero_form': web_hero_form,
        'card_form': card_form,
        'partner_form': partner_form,
        'footer_form': footer_form,
    })
