from django.views.generic import TemplateView


class ReportsView(TemplateView):
    template_name = "reports/reports.html"
