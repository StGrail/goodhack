from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget, Select

from .models import ExhibitionApplication, QuizzesForStudentsApplication


class ExhibitionApplicationForm(ModelForm):
    class Meta:
        model = ExhibitionApplication
        exclude = ['completed']
        widgets = {'date': SelectDateWidget()}


class QuizzesApplicationForm(ModelForm):
    class Meta:
        model = QuizzesForStudentsApplication
        exclude = ['completed']
        widgets = {'date': SelectDateWidget(),
                   'quiz_format': Select(choices=QuizzesForStudentsApplication.QUIZ_TYPES,
                                         ),
                   }
