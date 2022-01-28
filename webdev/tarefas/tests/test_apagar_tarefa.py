import pytest
from django.urls import reverse

from webdev.tarefas.models import Tarefa


@pytest.fixture
def tarefa(db, usuario_logado):
    return Tarefa.objects.create(nome='Tarefa1', feita=True, usuario=usuario_logado)


@pytest.fixture
def resp(client_com_usuario_logado, tarefa):
    return client_com_usuario_logado.post(reverse('tarefas:apagar', kwargs={'tarefa_id': tarefa.id}))


def test_apagar_tarefa(client_com_usuario_logado, resp):
    assert not Tarefa.objects.exists()
