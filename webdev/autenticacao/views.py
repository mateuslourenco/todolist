from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


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
