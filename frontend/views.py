from django.views.generic import TemplateView
from datetime import date

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Home'
        context['hostname'] = self.request.META['HTTP_HOST']
        context['date'] = date.today()
        return context



class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'About'
        context['hostname'] = self.request.META['HTTP_HOST']
        context['date'] = date.today()
        return context

class ServicesView(TemplateView):
    template_name = 'services.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Services'
        context['hostname'] = self.request.META['HTTP_HOST']
        context['date'] = date.today()
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Contact'
        context['hostname'] = self.request.META['HTTP_HOST']
        context['date'] = date.today()
        return context

class TermsView(TemplateView):
    template_name = 'terms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Terms'
        context['hostname'] = self.request.META['HTTP_HOST']
        context['date'] = date.today()
        return context

class PrivacyView(TemplateView):
    template_name = 'privacy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Privacy'
        context['hostname'] = self.request.META['HTTP_HOST']
        context['date'] = date.today()
        return context

class CookiePolicyView(TemplateView):
    template_name = 'cookie_policy.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Cookies'
        context['hostname'] = self.request.META['HTTP_HOST']
        context['date'] = date.today()
        return context
