from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from webdev.tarefas.forms import TarefaNovaForm, TarefaForm
from webdev.tarefas.models import Tarefa


@login_required
def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.usuario = request.user
            tarefa.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            tarefas_pendetes = Tarefa.objects.filter(feita=False, usuario_id=request.user).all()
            tarefas_feitas = Tarefa.objects.filter(feita=True, usuario_id=request.user).all()
            return render(
                request, 'tarefas/home.html',
                {
                    'form': form,
                    'tarefas_pendentes': tarefas_pendetes,
                    'tarefas_feitas': tarefas_feitas
                },
                status=400)
    tarefas_pendetes = Tarefa.objects.filter(feita=False, usuario_id=request.user).all()
    tarefas_feitas = Tarefa.objects.filter(feita=True, usuario_id=request.user).all()

    return render(
        request, 'tarefas/home.html',
        {
            'tarefas_pendentes': tarefas_pendetes,
            'tarefas_feitas': tarefas_feitas
        }
    )


def detalhe(request, tarefa_id):
    if request.method == 'POST':
        tarefa = Tarefa.objects.get(id=tarefa_id)
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
    return HttpResponseRedirect(reverse('tarefas:home'))


def apagar(request, tarefa_id):
    if request.method == 'POST':
        Tarefa.objects.filter(id=tarefa_id).delete()
    return HttpResponseRedirect(reverse('tarefas:home'))


def registrar(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('tarefas:home'))

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password2')
                user = authenticate(username=username, password=password)
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})
