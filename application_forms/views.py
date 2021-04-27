from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

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
            form.save()
            messages.success(request, 'Ваша заявка была принята. С Вами свяжутся в течение двух недель.')
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
            messages.success(request, 'Ваша заявка была принята. С Вами свяжутся в течение двух недель.')
            return redirect('index')
        else:
            print(form.errors)
            messages.warning(request, 'Произошла ошибка. Заполните заявку еще раз.')
            form = self.form_class()

        return render(request, self.template_name, {'form': form})


class ExhibitionReportsView(ListView):
    model = ExhibitionApplication
    template_name = 'tables/exhibition_table.html'

    def get_queryset(self):
        queryset = ExhibitionApplication.objects.filter(completed=True).values()
        return queryset


class QuizzesReportsView(ListView):
    model = QuizzesForStudentsApplication
    template_name = 'tables/quizzes_table.html'

    def get_queryset(self):
        queryset = QuizzesForStudentsApplication.objects.filter(completed=True).values()
        return queryset
