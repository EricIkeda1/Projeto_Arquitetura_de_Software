from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import user_passes_test, login_required
from .forms import ProdutoForm
from .models import Produto
from .forms import FabricanteForm
from django.contrib.admin.views.decorators import staff_member_required
from .models import Grupo, Subgrupo
from .forms import GrupoForm, SubgrupoForm

# View de login
@csrf_protect
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
                return redirect('inicio')
        
        return HttpResponse('Email ou senha inválidos')

# View de gráficos
@login_required
def graficos(request):
    return render(request, 'graficos.html')

# View de registro
@csrf_protect
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

# View de início
@login_required    
def inicio(request):
    return render(request, 'inicio.html')

#Cadastro de produtos
def is_admin(user):
    return user.is_staff

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='acesso_negado')
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'adicionar_produto.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

def acesso_negado(request):
    return render(request, 'acesso_negado.html')

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='acesso_negado')
def cadastrar_fabricante(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')
    else:
        form = FabricanteForm()
    return render(request, 'cadastro_fabricante.html', {'form': form})

def pagina_sucesso(request):
    return render(request, 'pagina_sucesso.html')

def listar_grupos(request):
    grupos = Grupo.objects.all()
    return render(request, 'listar_grupos.html', {'grupos': grupos})

def adicionar_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos')
    else:
        form = GrupoForm()
    return render(request, 'adicionar_grupo.html', {'form': form})

def adicionar_subgrupo(request):
    if request.method == 'POST':
        form = SubgrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos')
    else:
        form = SubgrupoForm()
    return render(request, 'adicionar_subgrupo.html', {'form': form})