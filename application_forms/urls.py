from django.urls import path

from application_forms.views import ExhibitionApplicationView, QuizzesApplicationView

urlpatterns = [
    path('exhibition_application_form', ExhibitionApplicationView.as_view(), name='exhibition_application_form'),
    path('quizzes_application_form', QuizzesApplicationView.as_view(), name='quizzes_application_form'),
]
