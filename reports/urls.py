from django.urls import path

from reports.views import ReportsList, ReportDetail

urlpatterns = [
    path('reports', ReportsList.as_view(), name='reports'),
    path('reports/<int:id>/', ReportDetail.as_view(), name='report'),
]
