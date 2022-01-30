import pytest
from django.urls import reverse
from model_mommy import mommy


@pytest.fixture
def usuario(db, django_user_model):
    usuario_criado = mommy.make(django_user_model)
    return usuario_criado


@pytest.fixture
def resp(client):
    return client.get(reverse('tarefas:registrar'))


def test_status_code(resp):
    assert resp.status_code == 200


@pytest.fixture
def resp_post(client, db, usuario):
    return client.post(reverse('tarefas:registrar'),
                       {
                           'username': f'{usuario.username}123',
                           'password1': usuario.password,
                           'password2': usuario.password,
                        })


def test_registrar_redirect(resp_post):
    assert resp_post.status_code == 302
    assert resp_post.url == reverse('tarefas:home')
