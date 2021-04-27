from django.urls import path

from application_forms.views import ExhibitionApplicationView, QuizzesApplicationView, ExhibitionReportsView, \
    QuizzesReportsView

urlpatterns = [
    path('exhibition_application_form', ExhibitionApplicationView.as_view(), name='exhibition_application_form'),
    path('quizzes_application_form', QuizzesApplicationView.as_view(), name='quizzes_application_form'),
    path('exhibition_reports', ExhibitionReportsView.as_view(), name='exhibition_reports'),
    path('quizzes_reports', QuizzesReportsView.as_view(), name='quizzes_reports'),
]
