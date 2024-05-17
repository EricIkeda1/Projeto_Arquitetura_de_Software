from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(email=email).first()
        
        if user is not None:
            user_auth = authenticate(request, username=user.username, password=senha)
            if user_auth is not None:
                login(request, user_auth)
                return redirect('tela_de_graficos')
        
        return HttpResponse('Email ou senha inválidos')

@login_required
def tela_de_graficos(request):
    return HttpResponse('graficos')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if not username or not email or not senha:
            error_message = 'Todos os campos são obrigatórios'
            return render(request, 'Cadastro.html', {'error_message': error_message})

        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            error_message = 'Já existe um usuário com este email'
            return render(request, 'Cadastro.html', {'error_message': error_message})

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        success_message = 'Usuário cadastrado com sucesso'
        return render(request, 'Cadastro.html', {'success_message': success_message})
    else:
        return render(request, 'Cadastro.html')