import pytest
from django.urls import reverse
from webdev.tarefas.models import Tarefa


@pytest.fixture
def resp(client_com_usuario_logado, db, usuario_logado):
    return client_com_usuario_logado.post(reverse('tarefas:home'), data={'nome': 'Tarefa', 'usuario': usuario_logado})


def test_tarefa_existe_no_bd(resp):
    assert Tarefa.objects.exists()


def test_redirecionamento_depois_do_salvamento(resp):
    assert resp.status_code == 302


@pytest.fixture
def resp_dado_invalido(client_com_usuario_logado, db):
    return client_com_usuario_logado.post(reverse('tarefas:home'), data={'nome': ''})


def test_tarefa_nao_existe_no_bd(resp_dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagina_com_dados_invalidos(resp_dado_invalido):
    assert resp_dado_invalido.status_code == 400
