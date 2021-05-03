import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_index_view(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'web/index.html')


def test_about_view(client):
    url = reverse('about')
    response = client.get(url)
    assert response.status_code == 200
    assertTemplateUsed(response, 'web/about.html')
