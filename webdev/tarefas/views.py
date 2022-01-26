from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tarefas.forms import TarefaNovaForm
from webdev.tarefas.models import Tarefa


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendetes = Tarefa.objects.filter(feita=False).all()
            return render(request, 'tarefas/home.html', {'form': form, 'tarefas_pendentes': tarefas_pendetes},
                          status=400)
    tarefas_pendetes = Tarefa.objects.filter(feita=False).all()
    return render(request, 'tarefas/home.html', {'tarefas_pendentes': tarefas_pendetes})
