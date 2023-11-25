from django import forms
from .models import WebHero, Card, Partner, Footer


class WebHeroForm(forms.ModelForm):
    class Meta:
        model = WebHero
        fields = ['cars_count',
                  'volunteers_count',
                  'shelter_refugees_count',
                  'days_of_war',
                  'days_of_rfu',
                  'humanitarian_goods_weight',
                  'flights_count']


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['image', 'title', 'description', 'button']


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['logo', 'url']


class FooterForm(forms.ModelForm):
    class Meta:
        model = Footer
        fields = ['address', 'legal_links']
