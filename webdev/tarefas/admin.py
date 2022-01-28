from django.contrib.admin import ModelAdmin, register

from webdev.tarefas.models import Tarefa


@register(Tarefa)
class TarefaAdmin(ModelAdmin):
    list_display = ('nome', 'feita', 'criada_em', 'usuario')
    list_filter = ('usuario',)
    ordering = ('criada_em',)
