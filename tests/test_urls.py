import pytest
from django.urls import reverse


def test_index_url_is_resolves(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_about_url_is_resolves(client):
    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200


def test_exhibition_application_form_url_is_resolves(client):
    url = reverse('exhibition_application_form')
    response = client.get(url)
    assert response.status_code == 200


def test_quizzes_application_form_url_is_resolves(client):
    url = reverse('quizzes_application_form')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_exhibition_reports_url_is_resolves(client):
    url = reverse('exhibition_reports')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_quizzes_reports_url_is_resolves(client):
    url = reverse('quizzes_reports')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_reports_url_is_resolves(client):
    url = reverse('reports')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.xfail
@pytest.mark.django_db
def test_report_detail_url_is_resolves(client):
    url = reverse('reports/1')
    response = client.get(url)
    assert response.status_code == 200
