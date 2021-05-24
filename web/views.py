from django.views.generic import TemplateView, ListView

from application_forms.models import ExhibitionApplication, QuizzesForStudentsApplication


class IndexView(ListView):
    template_name = "web/index.html"

    def get_queryset(self):
        exhibitions = ExhibitionApplication.objects.filter(completed=True).values().count()
        quizzes = QuizzesForStudentsApplication.objects.filter(completed=True).values().count()
        return exhibitions, quizzes


class AboutView(TemplateView):
    template_name = "web/about.html"


class ContactsView(TemplateView):
    template_name = "web/contacts.html"
