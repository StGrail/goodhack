from django.views.generic import ListView, DetailView

from reports.models import Report


class ReportsList(ListView):
    queryset = Report.objects.filter(status="Опубликовано").order_by('-created_on')
    template_name = "reports/reports.html"


class ReportDetail(DetailView):
    model = Report
    template_name = 'post_detail.html'
