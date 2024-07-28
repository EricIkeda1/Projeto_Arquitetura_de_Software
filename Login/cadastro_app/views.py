from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
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
from django.http import HttpResponseForbidden
from .models import Produto, Venda, VendaItem
from django.db import transaction
from django.utils import timezone
from .models import Venda
from django.http import HttpResponseRedirect
from django.urls import reverse
#import plotly.graph_objects as go
#import plotly.express as px
#from django.db.models import Sum
#from .graficos import get_vendas_data, get_venda_items_data, get_produtos_data, create_fig_linha, create_fig_barras, create_fig_dispersao, create_fig_pizza, create_fig_barras_linha
#from .graficos import get_estoque_baixo

# View de login
@csrf_protect
def login_view(request):
    if request.method == "GET":
        return render(request, 'Login.html')
    else:
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        user = User.objects.filter(email=email).first()
        
        if user is not None:
            user_auth = authenticate(request, username=user.username, password=senha)
            if user_auth is not None:
                login(request, user_auth)
                return redirect('Inicio')
        
        return HttpResponse('Email ou senha inválidos')

# View de gráficos
@login_required
def graficos(request):
    return render(request, 'Graficos.html')

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
    return render(request, 'Inicio.html')

#Cadastro de produto
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

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='acesso_negado')
def adicionar_subgrupo(request):
    if request.method == 'POST':
        form = SubgrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_grupos')
    else:
        form = SubgrupoForm()
    return render(request, 'adicionar_subgrupo.html', {'form': form})

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'listar_produtos.html', {'produtos': produtos})

@login_required(login_url='login')
@user_passes_test(is_admin, login_url='acesso_negado')
def remover_produto(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)
    
    if request.method == 'POST':
        produto.delete()
        return redirect('listar_produtos')
    else:
        return HttpResponseForbidden("Acesso negado")

def remover_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == "POST":
        produto.delete()
        return redirect('listar_produtos') 
    return redirect('listar_produtos')  

def adicionar_venda(request):
    if request.method == 'POST':
        itens = request.POST.getlist('itens')  # Lista de IDs de produtos
        quantidades = request.POST.getlist('quantidades')  # Lista de quantidades
        with transaction.atomic():
            venda = Venda.objects.create()
            valor_total = 0
            for item_id, quantidade in zip(itens, quantidades):
                produto = get_object_or_404(Produto, id=item_id)
                quantidade = int(quantidade)
                valor_item = produto.preco_venda * quantidade
                VendaItem.objects.create(venda=venda, produto=produto, quantidade=quantidade, valor_total=valor_item)
                valor_total += valor_item
            venda.valor_total = valor_total
            venda.save()
        return redirect('venda_detalhe', venda_id=venda.id)
    else:
        produtos = Produto.objects.all()
        return render(request, 'adicionar_venda.html', {'produtos': produtos})


def graficos(request):
#    # Dados para os gráficos
#    vendas = get_vendas_data()
#    venda_items = get_venda_items_data()
#    produtos = get_produtos_data()

    # Gráfico de Linha: Custo Total e Valor Venda Total Mensal
#    fig_linha = create_fig_linha(vendas, produtos)

    # Gráfico de Barras: Quantidade Comprada Total e Quantidade Vendida Total Mensal
#    fig_barras = create_fig_barras(vendas, produtos)

    # Gráfico de Dispersão: Percentual de Lucro dos Produtos Vendidos
#   fig_dispersao = create_fig_dispersao(venda_items, produtos)

    # Gráfico de Pizza: 3 Produtos Mais Vendidos em Quantidade
#    fig_pizza = create_fig_pizza(produtos)

    # Gráfico de Barras e Linha: 4 Grupos de Produtos Mais Vendidos com Meta >= 1000 Unidades
#    fig_barras_linha = create_fig_barras_linha(produtos)

    # Tabela Analítica: Produtos com Estoque Baixo
#    estoque_baixo = get_estoque_baixo()

#    context = {
#        'fig_linha': fig_linha.to_html(),
#        'fig_barras': fig_barras.to_html(),
#        'fig_dispersao': fig_dispersao.to_html(),
#        'fig_pizza': fig_pizza.to_html(),
#        'fig_barras_linha': fig_barras_linha.to_html(),
#       'estoque_baixo': estoque_baixo,
#    }

    return render(request, 'graficos.html',) #context)

@login_required
def venda_detalhe(request, venda_id):
    venda = get_object_or_404(Venda, pk=venda_id)
    venda_items = venda.itens.all()

    context = {
        'venda': venda,
        'venda_items': venda_items,
    }
    return render(request, 'venda_detalhe.html', context)

def rede_social(request):
    return render(request, 'rede_sociais.html')