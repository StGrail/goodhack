from django.forms import ModelForm
from django.forms.widgets import SelectDateWidget

from .models import ExhibitionApplication, QuizzesForStudentsApplication


class ExhibitionApplicationForm(ModelForm):
    class Meta:
        model = ExhibitionApplication
        exclude = ['completed']

    def __init__(self, *args, **kwargs):
        super(ExhibitionApplicationForm, self).__init__(*args, **kwargs)
        self.fields['exhibition_date'].widget = SelectDateWidget()


class QuizzesForm(ModelForm):
    class Meta:
        model = QuizzesForStudentsApplication
        exclude = ['completed']

    def __init__(self, *args, **kwargs):
        super(QuizzesForm, self).__init__(*args, **kwargs)
        self.fields['exhibition_date'].widget = SelectDateWidget()
