from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "web/index.html"


class AboutView(TemplateView):
    template_name = "web/about.html"


class ContactsView(TemplateView):
    template_name = "web/contacts.html"
