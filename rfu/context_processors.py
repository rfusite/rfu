# context_processors.py
from cookie_consent.models import CookieGroup
from cookie_consent.util import get_cookie_value_from_request

from rfu.main_page.models import Footer, CookiesConsent


def cookie_settings(request):
    cookie_groups = CookieGroup.objects.all()
    current_settings = {group.varname: request.COOKIES.get(group.varname, 'False') == 'True'
                        for group in cookie_groups}
    consent_cookie = get_cookie_value_from_request(request, 'cookie_consent')
    cookies_consent = CookiesConsent.objects.first()
    show_cookie_banner = consent_cookie is None
    return {
        'cookie_groups': cookie_groups,
        'current_settings': current_settings,
        'show_cookie_banner': show_cookie_banner,
        'cookies_consent': cookies_consent
    }


def footer_context(request):
    return {
        'footer': Footer.objects.first()
    }
