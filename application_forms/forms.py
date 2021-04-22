from django.forms import ModelForm
from django.contrib.admin import widgets

from .models import ExhibitionApplication, QuizzesForStudentsApplication


class ExhibitionApplicationForm(ModelForm):
    class Meta:
        model = ExhibitionApplication
        exclude = ['completed']

    # def __init__(self, *args, **kwargs):
    #     super(ExhibitionApplicationForm, self).__init__(*args, **kwargs)
    #     self.fields['exhibition_date'].widget = widgets.AdminSplitDateTime()


class QuizzesForm(ModelForm):
    class Meta:
        model = QuizzesForStudentsApplication
        exclude = ['completed']
