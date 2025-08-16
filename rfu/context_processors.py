# context_processors.py
from rfu.main_page.models import Footer, CookiesConsent


def cookie_settings(request):
    cookies_consent = CookiesConsent.objects.first()
    cookie_consent = request.COOKIES.get('cookie_consent_accepted')
    show_cookie_banner = not cookie_consent
    analytics_accepted = request.COOKIES.get('analytics_cookies', 'false') == 'true'
    marketing_accepted = request.COOKIES.get('marketing_cookies', 'false') == 'true'
    functional_accepted = request.COOKIES.get('functional_cookies', 'false') == 'true'
    
    return {
        'show_cookie_banner': show_cookie_banner,
        'cookies_consent': cookies_consent,
        'analytics_accepted': analytics_accepted,
        'marketing_accepted': marketing_accepted,
        'functional_accepted': functional_accepted,
    }


def footer_context(request):
    return {
        'footer': Footer.objects.first()
    }
