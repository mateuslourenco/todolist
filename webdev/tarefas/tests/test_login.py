import pytest
from django.urls import reverse
from model_mommy import mommy

from webdev.django_assertions import assert_contains, assert_not_contains


@pytest.fixture
def resp(client):
    return client.get(reverse('login'))


def test_login_form_page(resp):
    assert resp.status_code == 200


def test_botao_login_disponivel(resp):
    assert_contains(resp, 'Logar')


def test_botao_registrar_disponivel(resp):
    assert_contains(resp, 'Registre-se')


def test_link_registrar_disponivel(resp):
    assert_contains(resp, reverse('tarefas:registrar'))


@pytest.fixture
def usuario(db, django_user_model):
    usuario_modelo = mommy.make(django_user_model)
    senha = 'senha'
    usuario_modelo.set_password(senha)
    usuario_modelo.save()
    usuario_modelo.senha_plana = senha
    return usuario_modelo


@pytest.fixture
def resp_post(client, usuario):
    return client.post(reverse('login'), {'username': usuario.username, 'password': usuario.senha_plana})


def test_login_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('tarefas:home')


@pytest.fixture
def resp_home_com_usuario_logado(client_com_usuario_logado, db):
    return client_com_usuario_logado.get(reverse('tarefas:home'))


def test_nome_usuario_disponivel(resp_home_com_usuario_logado, usuario_logado):
    username_capitalize = str(usuario_logado.username).capitalize()
    assert_contains(resp_home_com_usuario_logado, f'Olá {username_capitalize}!')


def test_botao_sair_disponivel(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, 'Sair')


def test_link_de_logout_disponivel(resp_home_com_usuario_logado):
    assert_contains(resp_home_com_usuario_logado, reverse('logout'))


def test_nome_usuario_indisponivel(resp, usuario_logado):
    username_capitalize = str(usuario_logado.username).capitalize()
    assert_not_contains(resp, f'Olá {username_capitalize}!')


def test_botao_sair_indisponivel(resp):
    assert_not_contains(resp, 'Sair')


def test_link_de_logout_indisponivel(resp):
    assert_not_contains(resp, reverse('logout'))
