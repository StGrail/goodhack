from django.urls import path

from reports.views import ReportsView

urlpatterns = [
    path('reports', ReportsView.as_view(), name='reports'),
]
