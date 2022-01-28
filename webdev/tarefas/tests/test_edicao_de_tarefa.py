import pytest
from django.urls import reverse

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa_pendente(db, usuario_logado):
    return Tarefa.objects.create(nome='Tarefa1', feita=False, usuario=usuario_logado)


@pytest.fixture
def resp_com_tarefa_pendente(client_com_usuario_logado, tarefa_pendente):
    return client_com_usuario_logado.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_pendente.id}),
        data={'feita': 'true', 'nome': f'{tarefa_pendente.nome}-editada'}
    )


def test_status_code(resp_com_tarefa_pendente):
    assert resp_com_tarefa_pendente.status_code == 302


def test_tarefa_feita(resp_com_tarefa_pendente):
    assert Tarefa.objects.first().feita


@pytest.fixture
def tarefa_feita(db, usuario_logado):
    return Tarefa.objects.create(nome='Tarefa1', feita=True, usuario=usuario_logado)


@pytest.fixture
def resp_com_tarefa_feita(client_com_usuario_logado, tarefa_feita):
    return client_com_usuario_logado.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_feita.id}),
        data={'nome': f'{tarefa_feita.nome}-editada'}
    )


def test_tarefa_pendente(resp_com_tarefa_feita):
    assert not Tarefa.objects.first().feita
