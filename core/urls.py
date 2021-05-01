from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
    path('', include('application_forms.urls')),
    path('', include('reports.urls')),
]
