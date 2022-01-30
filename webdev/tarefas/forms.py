from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from webdev.tarefas.models import Tarefa


class TarefaNovaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome']


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'feita']


class NovoUsuario(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NovoUsuario, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
