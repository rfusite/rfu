from django import forms
from .models import WebHero, Card, Partner, Footer


class WebHeroForm(forms.ModelForm):
    class Meta:
        model = WebHero
        fields = ['image']


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
