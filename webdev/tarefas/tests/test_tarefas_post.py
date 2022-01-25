import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains
from webdev.tarefas.models import Tarefa


@pytest.fixture
def resp(client, db):
    return client.post(reverse('tarefas:home'), data={'nome': 'Tarefa'})


def test_tarefa_existe_no_bd(resp):
    assert Tarefa.objects.exists()


def test_redirecionamento_depois_do_salvamento(resp):
    assert resp.status_code == 302


@pytest.fixture
def resp_dado_invalido(client, db):
    return client.post(reverse('tarefas:home'), data={'nome': ''})


def test_tarefa_nao_existe_no_bd(resp_dado_invalido):
    assert not Tarefa.objects.exists()


def test_pagina_com_dados_invalidos(resp_dado_invalido):
    assert resp_dado_invalido.status_code == 400
