from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from webdev.tarefas.forms import TarefaNovaForm, TarefaForm, NovoUsuarioForm
from webdev.tarefas.models import Tarefa, User


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
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            if User.objects.filter(username=username).first():
                messages.error(request, "Usuário inválido")
                return redirect('tarefas:registrar')
            elif len(password) < 8:
                messages.error(request, "Senha inválida")
                return redirect('tarefas:registrar')
            else:
                usuario = User.objects.create_user(username=username, password=password)
                login(request, usuario)
                return HttpResponseRedirect(reverse('tarefas:home'))
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})
