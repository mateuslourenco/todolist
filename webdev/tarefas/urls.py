from django.urls import path
from webdev.tarefas import views

app_name = 'tarefas'
urlpatterns = [
    path('', views.home, name='home'),
    path('registrar', views.registrar, name='registrar'),
    path('<int:tarefa_id>', views.detalhe, name='detalhe'),
    path('apagar/<int:tarefa_id>', views.apagar, name='apagar'),
]
