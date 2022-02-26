import pytest
from django.urls import reverse
from model_bakery import baker

from webdev.django_assertions import assert_contains
from webdev.tarefas.models import User


@pytest.fixture
def usuario(db, django_user_model):
    usuario_criado = baker.make(django_user_model)
    return usuario_criado


@pytest.fixture
def resp(client):
    return client.get(reverse('tarefas:registrar'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture
def resp_com_usuario_criado(client, db, usuario):
    return client.post(reverse('tarefas:registrar'),
                       {
                           'username': 'novousername',
                           'password1': usuario.password,
                           'password2': usuario.password,
                        })


def test_registrar_redirect(resp_com_usuario_criado):
    assert resp_com_usuario_criado.status_code == 302
    assert resp_com_usuario_criado.url == reverse('tarefas:home')


def test_usuario_criado_no_db(resp_com_usuario_criado):
    assert User.objects.filter(username="novousername")


@pytest.fixture
def usuario_criado(db, usuario):
    return User.objects.create(username='usuario_criado', password='usuario.password')


@pytest.fixture
def resp_com_usuario_criado_ja_existente(client, db, usuario):
    return client.post(reverse('tarefas:registrar'),
                       {
                           'username': 'usuario_criado',
                           'password1': usuario.password,
                           'password2': usuario.password,
                        })


def test_usuario_criado_ja_existente(usuario_criado, resp_com_usuario_criado_ja_existente):
    assert_contains(resp_com_usuario_criado_ja_existente, 'Um usuário com este nome de usuário já existe.')


def test_usuario_logado_redirect(client_com_usuario_logado, resp):
    assert resp.status_code == 302
    assert resp.url == reverse('tarefas:home')


@pytest.fixture
def resp_com_senha_invalida(client, db, usuario):
    return client.post(reverse('tarefas:registrar'),
                       {
                           'username': usuario.username,
                           'password1': '1234',
                           'password2': '1234',
                        })


def test_senha_invalida(resp_com_senha_invalida):
    assert_contains(resp_com_senha_invalida, 'Esta senha')
