from django.urls import path
from .views import manage_page

app_name = 'main_page'


urlpatterns = [
    path('', manage_page, name='manage_page'),
]
