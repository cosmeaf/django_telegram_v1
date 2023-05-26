from django.urls import path
from .views import HomeView, AboutView, ServicesView, ContactView, TermsView, PrivacyView, CookiePolicyView

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServicesView.as_view(), name='services'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('terms/', TermsView.as_view(), name='terms'),
    path('privacy/', PrivacyView.as_view(), name='privacy'),
    path('cookie-policy/', CookiePolicyView.as_view(), name='cookie_policy'),
]
