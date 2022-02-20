# todolist

Código desenvolvido no módulo de [Imersão Django](https://www.youtube.com/watch?v=zLIeu9cPYrY&list=PLA05yVJtRWYRgtGyrdH4Bbf2gtbk6OtTu&ab_channel=CanalPythonProBr) do [Site Python Pro](https://www.python.pro.br)

Projeto disponível em https://todolist-django-m.herokuapp.com/

[![Django CI](https://github.com/mateuslourenco/todolist/actions/workflows/django.yml/badge.svg)](https://github.com/mateuslourenco/todolist/actions/workflows/django.yml)
[![Updates](https://pyup.io/repos/github/mateuslourenco/todolist/shield.svg)](https://pyup.io/repos/github/mateuslourenco/todolist/)
[![Python 3](https://pyup.io/repos/github/mateuslourenco/todolist/python-3-shield.svg)](https://pyup.io/repos/github/mateuslourenco/todolist/)


## Descrição

Projeto "To Do LIst" é um checklist construído com Django para treinar as funções básicas de CRUD e boas prátricas de programação. Foram utilizados conceitos da metodologia Twelve-Factor App. 

Neste projeto é possível cadastrar um novo usuário, realizar login, além de adicionar, modificar e excluir tarefas

## Como rodar o projeto localmente

- Clone esse repositório
- Instale o pipenv 
- Instale as dependencias
- Copie as variáveis de ambiante
- Inicie o banco de dados postgres com docker
- Rode as migrações


```
git clone https://github.com/mateuslourenco/todolist.git
cd todolist
python -m pip install pipenv
pipenv sync -d
cp contrib/env-sample .env
docker-compose up -d
pipenv run python manage.py migrate
pipenv run python manage.py runserver
```
