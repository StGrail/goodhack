from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from application_forms.forms import ExhibitionApplicationForm, QuizzesApplicationForm


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
            messages.warning(request, 'Произошла ошибка. Заполните заявку еще раз.')
            form = self.form_class()

        return render(request, self.template_name, {'form': form})
