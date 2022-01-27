from django.contrib.admin import ModelAdmin, register

from webdev.tarefas.models import Tarefa


@register(Tarefa)
class TarefaAdmin(ModelAdmin):
    list_display = ('nome', 'feita', 'criada_em')
    ordering = ('criada_em',)
