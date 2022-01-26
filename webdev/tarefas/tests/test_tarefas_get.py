import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def resp(client, db):
    return client.get(reverse('tarefas:home'))


def test_status_code(client, resp):
    assert resp.status_code == 200


def test_formulario_presente(client, resp):
    assertContains(resp, '<form')


def test_botao_salvar_presente(client, resp):
    assertContains(resp, '<button type="submit"')



@pytest.fixture
def lista_de_tarefas_pendentes(db):
    tarefas = [
        Tarefa(nome='Tarefa1', feita=False),
        Tarefa(nome='Tarefa2', feita=False),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resp_com_lista_de_tarefas(client, lista_de_tarefas_pendentes):
    return client.get(reverse('tarefas:home'))


def test_listar_de_tarefas_pendentes_presentes(client, resp_com_lista_de_tarefas, lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resp_com_lista_de_tarefas, tarefa.nome)
