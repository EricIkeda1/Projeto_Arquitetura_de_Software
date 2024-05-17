from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_view(request):
    if request.method == "GET":
        return render(request, 'Login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            login(request, user)
            
            return HttpResponse('autenticado') 
        else:
            return HttpResponse('Email ou senha invalidos')   

@login_required
def tela_de_graficos(request):
        return HttpResponse('graficos')

def register_view(request):
    if request.method == "GET":
        return render(request, 'Cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user_exists = User.objects.filter(username=username).exists()

        if user_exists:
            return HttpResponse('Já existe um usuário com este username')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
            
        return HttpResponse('Usuário cadastrado com sucesso')


