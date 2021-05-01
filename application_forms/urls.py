from django.urls import path

from application_forms.views import ExhibitionApplicationView, QuizzesApplicationView, ExhibitionTableView, \
    QuizzesTableView

urlpatterns = [
    path('exhibition_application_form', ExhibitionApplicationView.as_view(), name='exhibition_application_form'),
    path('quizzes_application_form', QuizzesApplicationView.as_view(), name='quizzes_application_form'),
    path('exhibition_reports', ExhibitionTableView.as_view(), name='exhibition_reports'),
    path('quizzes_reports', QuizzesTableView.as_view(), name='quizzes_reports'),
]
