import pytest
from django.urls import reverse

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa_pendente(db):
    return Tarefa.objects.create(nome='Tarefa1', feita=False)


@pytest.fixture
def resp_com_tarefa_pendente(client, tarefa_pendente):
    return client.post(
        reverse('tarefas:detalhe', kwargs={'tarefa_id': tarefa_pendente.id}),
        data={'feita': 'true', 'nome': f'{tarefa_pendente.nome}-editada'}
    )


def test_status_code(resp_com_tarefa_pendente):
    assert resp_com_tarefa_pendente.status_code == 302


def test_tarefa_feita(resp_com_tarefa_pendente):
    assert Tarefa.objects.first().feita
