from django.views.generic import ListView, DetailView

from reports.models import Report


class ReportsList(ListView):
    queryset = Report.objects.filter(status='Опубликовано')
    template_name = 'reports/reports.html'
    paginate_by = 5


class ReportDetail(DetailView):
    model = Report
    template_name = 'reports/report.html'

    def get_object(self, queryset=None):
        return Report.objects.get(id=self.kwargs.get("id"))
