import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from webdev.tarefas.models import Tarefa


@pytest.fixture
def resp(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('tarefas:home'))


def test_status_code(resp):
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
def lista_de_tarefas_feitas(db):
    tarefas = [
        Tarefa(nome='Tarefa3', feita=True),
        Tarefa(nome='Tarefa4', feita=True),
    ]
    Tarefa.objects.bulk_create(tarefas)
    return tarefas


@pytest.fixture
def resp_com_lista_de_tarefas(client, lista_de_tarefas_pendentes, lista_de_tarefas_feitas):
    return client.get(reverse('tarefas:home'))


def test_listar_de_tarefas_pendentes_presentes(client_com_usuario_logado, resp_com_lista_de_tarefas,
                                               lista_de_tarefas_pendentes):
    for tarefa in lista_de_tarefas_pendentes:
        assertContains(resp_com_lista_de_tarefas, tarefa.nome)


def test_listar_de_tarefas_feitas_presentes(client_com_usuario_logado, resp_com_lista_de_tarefas,
                                            lista_de_tarefas_feitas):
    for tarefa in lista_de_tarefas_feitas:
        assertContains(resp_com_lista_de_tarefas, tarefa.nome)
