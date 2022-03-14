from django.urls import path
from webdev.autenticacao import views

app_name = 'autenticacao'
urlpatterns = [
    path('registrar', views.registrar, name='registrar'),
]
