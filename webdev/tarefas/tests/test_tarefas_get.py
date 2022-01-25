import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains


@pytest.fixture
def resp(client):
    return client.get(reverse('tarefas:home'))


def test_status_code(client, resp):
    assert resp.status_code == 200


def test_formulario_presente(client, resp):
    assertContains(resp, '<form')


def test_botao_salvar_presente(client, resp):
    assertContains(resp, '<button type="submit"')
