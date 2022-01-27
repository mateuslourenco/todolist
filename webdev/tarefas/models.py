from django.db import models


class Tarefa(models.Model):
    nome = models.CharField(max_length=128)
    feita = models.BooleanField(default=False)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Tarefa {self.nome}'
