from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from reports.views import ReportsList, ReportDetail

urlpatterns = [
    path('reports', ReportsList.as_view(), name='reports'),
    path('reports/<int:id>', ReportDetail.as_view(), name='report'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
