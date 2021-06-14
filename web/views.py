from django.db.models import Sum
from django.views.generic import TemplateView, ListView

from application_forms.models import ExhibitionApplication, QuizzesForStudentsApplication


class IndexView(TemplateView):
    template_name = "web/index.html"

    def get_context_data(self, **kwargs):
        exhibitions_cities = ExhibitionApplication.objects.filter(completed=True).values('city').count()
        quizzes_cities = QuizzesForStudentsApplication.objects.filter(completed=True).values('city').count()
        exhibitions_total = ExhibitionApplication.objects.filter(completed=True).count()
        quizzes_total = QuizzesForStudentsApplication.objects.filter(completed=True).count()
        exhibitions_visitors = ExhibitionApplication.objects.filter(completed=True).aggregate(Sum('visitors_number'))
        quizzes_visitors = QuizzesForStudentsApplication.objects.filter(completed=True).aggregate(
            Sum('visitors_number'))

        total_cities = exhibitions_cities + quizzes_cities
        if exhibitions_visitors['visitors_number__sum'] and quizzes_visitors['visitors_number__sum'] is not None:
            total_visitors = exhibitions_visitors['visitors_number__sum'] + quizzes_visitors['visitors_number__sum']
        elif exhibitions_visitors is None and quizzes_visitors is not None:
            total_visitors = quizzes_visitors['visitors_number__sum']
        elif exhibitions_visitors is not None and quizzes_visitors is None:
            total_visitors = exhibitions_visitors['visitors_number__sum']
        else:
            total_visitors = 0

        context = {
            'cities': total_cities,
            'exhibitions': exhibitions_total,
            'quizzes': quizzes_total,
            'visitors': total_visitors,
        }
        return context


class AboutView(TemplateView):
    template_name = "web/about.html"


class ContactsView(TemplateView):
    template_name = "web/contacts.html"
