from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, TemplateView

from application_forms.forms import ExhibitionApplicationForm, QuizzesApplicationForm
from application_forms.models import ExhibitionApplication, QuizzesForStudentsApplication


class ExhibitionApplicationView(View):
    form_class = ExhibitionApplicationForm
    template_name = 'application_forms/exhibition_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            contacts = form['contacts']
            print(contacts)
            form.save()
            send_mail(
                '«О, да, вторсырье!»',
                f'Новая заявка на проведение выставки!\n',
                ['zzmrlol@gmail.com'],
                ['zzmrlol@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Ваша заявка была принята. С Вами свяжутся в течение недели.')
            return redirect('index')
        else:
            print(form.errors)
            form = self.form_class()
            messages.warning(request, 'Произошла ошибка. Заполните заявку еще раз.')

        return render(request, self.template_name, {'form': form})


class QuizzesApplicationView(View):
    form_class = QuizzesApplicationForm
    template_name = 'application_forms/quizzes_form.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваша заявка была принята. С Вами свяжутся в течение недели.')
            return redirect('index')
        else:
            print(form.errors)
            messages.warning(request, 'Произошла ошибка. Заполните заявку еще раз.')
            form = self.form_class()

        return render(request, self.template_name, {'form': form})


class ExhibitionTableView(TemplateView):
    model = ExhibitionApplication
    template_name = 'tables/exhibition_table.html'

    def get_context_data(self, **kwargs):
        queryset = ExhibitionApplication.objects.filter(completed=True).values()
        total_exhibition = ExhibitionApplication.objects.filter(completed=True).count()
        total_cities = ExhibitionApplication.objects.filter(completed=True).values('city').count()
        total_organizes = ExhibitionApplication.objects.filter(completed=True).values('who_is_organize').count()
        total_places = ExhibitionApplication.objects.filter(completed=True).values('place').count()
        total_visitors = ExhibitionApplication.objects.filter(completed=True).aggregate(Sum('visitors_number'))
        total_reports = ExhibitionApplication.objects.filter(completed=True).values('link').count()

        #  Проверяем, что кол-во участников не None
        if total_visitors['visitors_number__sum'] is not None:
            total_visitors = total_visitors['visitors_number__sum']
        else:
            total_visitors = '-'

        total = {
            "cities": total_cities,
            "organizes": total_organizes,
            "places": total_places,
            "visitors": total_visitors,
            "exhibitions": total_exhibition,
            "reports": total_reports,
        }
        context = {
            'queryset': queryset,
            'total': total,
        }
        return context


class QuizzesTableView(ListView):
    model = QuizzesForStudentsApplication
    template_name = 'tables/quizzes_table.html'

    def get_context_data(self, **kwargs):
        queryset = QuizzesForStudentsApplication.objects.filter(completed=True).values()
        total_exhibition = QuizzesForStudentsApplication.objects.filter(completed=True).count()
        total_cities = QuizzesForStudentsApplication.objects.filter(completed=True).values('city').count()
        total_organizes = QuizzesForStudentsApplication.objects.filter(completed=True).values('who_is_organize').count()
        total_places = QuizzesForStudentsApplication.objects.filter(completed=True).values('place').count()
        total_visitors = QuizzesForStudentsApplication.objects.filter(completed=True).aggregate(Sum('visitors_number'))
        total_reports = QuizzesForStudentsApplication.objects.filter(completed=True).values('link').count()

        #  Проверяем, что кол-во участников не None
        if total_visitors['visitors_number__sum'] is not None:
            total_visitors = total_visitors['visitors_number__sum']
        else:
            total_visitors = '0'

        total = {
            "cities": total_cities,
            "organizes": total_organizes,
            "places": total_places,
            "visitors": total_visitors,
            "exhibitions": total_exhibition,
            "reports": total_reports,
        }
        context = {
            'queryset': queryset,
            'total': total,
        }
        return context
