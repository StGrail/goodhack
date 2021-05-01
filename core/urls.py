from django.contrib import admin
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('', include('application_forms.urls')),
    path('', include('reports.urls')),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
