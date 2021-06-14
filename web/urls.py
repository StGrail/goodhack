from django.urls import path

from web.views import IndexView, AboutView, ContactsView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('contacts', ContactsView.as_view(), name='contacts'),
]
