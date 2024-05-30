from django.shortcuts import render
from django.db.models import Sum
from django.utils import timezone
from .models import Venda, Produto, VendaItem
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

def get_vendas_data():
    return Venda.objects.filter(data_hora_venda__year=timezone.now().year)

def get_venda_items_data():
    return VendaItem.objects.filter(venda__data_hora_venda__year=timezone.now().year)

def get_produtos_data():
    return Produto.objects.all()

def create_fig_linha(vendas, produtos):
    df_vendas = pd.DataFrame(list(vendas.values('data_hora_venda', 'valor_total')))
    df_produtos = pd.DataFrame(list(produtos.values('id', 'nome', 'preco_custo', 'preco_venda', 'quantidade_comprado', 'quantidade_vendido', 'grupo')))

    df_vendas['mes'] = df_vendas['data_hora_venda'].dt.month
    df_vendas_mensal = df_vendas.groupby('mes').agg({'valor_total': 'sum'}).reset_index()
    fig_linha = go.Figure()
    fig_linha.add_trace(go.Scatter(x=df_vendas_mensal['mes'], y=df_vendas_mensal['valor_total'], mode='lines+markers', name='Valor Venda Total'))

    df_produtos['mes'] = df_produtos['quantidade_vendido'] * df_produtos['preco_custo']
    fig_linha.add_trace(go.Scatter(x=df_produtos['mes'], y=df_produtos['quantidade_vendido'], mode='lines+markers', name='Valor Custo Total'))
    fig_linha.update_layout(title='Gráfico de Linha')

    return fig_linha

def create_fig_barras(vendas, produtos):
    df_vendas = pd.DataFrame(list(vendas.values('data_hora_venda', 'valor_total')))
    df_produtos = pd.DataFrame(list(produtos.values('id', 'nome', 'preco_custo', 'preco_venda', 'quantidade_comprado', 'quantidade_vendido', 'grupo')))

    df_produtos['mes'] = df_vendas['data_hora_venda'].dt.month
    df_produtos_mensal = df_produtos.groupby('mes').agg({'quantidade_comprado': 'sum', 'quantidade_vendido': 'sum'}).reset_index()
    fig_barras = go.Figure()
    fig_barras.add_trace(go.Bar(x=df_produtos_mensal['mes'], y=df_produtos_mensal['quantidade_comprado'], name='Quantidade Comprada'))
    fig_barras.add_trace(go.Bar(x=df_produtos_mensal['mes'], y=df_produtos_mensal['quantidade_vendido'], name='Quantidade Vendida'))
    fig_barras.update_layout(title='Gráfico de Barras')

    return fig_barras

def create_fig_dispersao(venda_items, produtos):
    df_venda_items = pd.DataFrame(list(venda_items.values('produto', 'quantidade', 'valor_total')))
    df_produtos = pd.DataFrame(list(produtos.values('id', 'preco_custo')))

    df_venda_items['lucro'] = (df_venda_items['valor_total'] - (df_venda_items['quantidade'] * df_produtos['preco_custo'])) / df_venda_items['valor_total']
    fig_dispersao = px.scatter(df_venda_items, x='produto', y='lucro', title='Gráfico de Dispersão')

    return fig_dispersao

def create_fig_pizza(produtos):
    df_produtos = pd.DataFrame(list(produtos.values('nome', 'quantidade_vendido')))
    top_produtos = df_produtos.nlargest(3, 'quantidade_vendido')
    fig_pizza = px.pie(top_produtos, values='quantidade_vendido', names='nome', title='Gráfico de Pizza')

    return fig_pizza

def create_fig_barras_linha(produtos):
    df_produtos = pd.DataFrame(list(produtos.values('grupo', 'quantidade_vendido')))
    df_grupo = df_produtos.groupby('grupo').agg({'quantidade_vendido': 'sum'}).reset_index()
    top_grupos = df_grupo[df_grupo['quantidade_vendido'] >= 1000].nlargest(4, 'quantidade_vendido')
    fig_barras_linha = go.Figure()
    fig_barras_linha.add_trace(go.Bar(x=top_grupos['grupo'], y=top_grupos['quantidade_vendido'], name='Quantidade Vendida'))
    fig_barras_linha.add_trace(go.Scatter(x=top_grupos['grupo'], y=[1000]*len(top_grupos), mode='lines+markers', name='Meta 1000 Unidades'))
    fig_barras_linha.update_layout(title='Gráfico de Barra e Linha')

    return fig_barras_linha

def get_estoque_baixo():
    return Produto.objects.filter(quantidade_comprado__lt=50).order_by('-quantidade_comprado')