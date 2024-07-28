# graficos.py
from django.utils import timezone
from .models import Venda, Produto, VendaItem
#import pandas as pd
#from django.db.models import Sum

def get_vendas_data():
    return Venda.objects.filter(data_hora_venda__year=timezone.now().year)

def get_venda_items_data():
    return VendaItem.objects.filter(venda__data_hora_venda__year=timezone.now().year)

def get_produtos_data():
    return Produto.objects.all()

def create_data_linha(vendas):
    df_vendas = pd.DataFrame(list(vendas.values('data_hora_venda', 'valor_total')))
    df_vendas['mes'] = df_vendas['data_hora_venda'].dt.month
    df_vendas_mensal = df_vendas.groupby('mes').agg({'valor_total': 'sum'}).reset_index()
    
    labels = df_vendas_mensal['mes'].astype(str).tolist()
    data = df_vendas_mensal['valor_total'].tolist()

    return labels, data

def create_data_barras(vendas, produtos):
    df_vendas = pd.DataFrame(list(vendas.values('data_hora_venda', 'valor_total')))
    df_produtos = pd.DataFrame(list(produtos.values('id', 'nome', 'quantidade_comprado', 'quantidade_vendido')))
    df_vendas['mes'] = df_vendas['data_hora_venda'].dt.month
    df_produtos['mes'] = df_vendas['mes']
    df_produtos_mensal = df_produtos.groupby('mes').agg({'quantidade_comprado': 'sum', 'quantidade_vendido': 'sum'}).reset_index()
    
    labels = df_produtos_mensal['mes'].astype(str).tolist()
    data_comprado = df_produtos_mensal['quantidade_comprado'].tolist()
    data_vendido = df_produtos_mensal['quantidade_vendido'].tolist()

    return labels, data_comprado, data_vendido

def create_data_dispersao(venda_items, produtos):
    df_venda_items = pd.DataFrame(list(venda_items.values('produto', 'quantidade', 'valor_total')))
    df_produtos = pd.DataFrame(list(produtos.values('id', 'preco_custo')))

    df_venda_items['lucro'] = (df_venda_items['valor_total'] - (df_venda_items['quantidade'] * df_produtos['preco_custo'])) / df_venda_items['valor_total']
    labels = df_venda_items['produto'].astype(str).tolist()
    data = df_venda_items['lucro'].tolist()

    return labels, data

def create_data_pizza(produtos):
    df_produtos = pd.DataFrame(list(produtos.values('nome', 'quantidade_vendido')))
    top_produtos = df_produtos.nlargest(3, 'quantidade_vendido')
    
    labels = top_produtos['nome'].tolist()
    data = top_produtos['quantidade_vendido'].tolist()

    return labels, data

def create_data_barras_linha(produtos):
    produtos_vendidos_ano_corrente = produtos.filter(vendaitem__venda__data_hora_venda__year=timezone.now().year)
    grupos_quantidade_vendida = produtos_vendidos_ano_corrente.values('grupo').annotate(total_vendido=Sum('quantidade_vendido'))
    
    top_grupos = sorted(grupos_quantidade_vendida, key=lambda x: x['total_vendido'], reverse=True)[:4]
    labels = [grupo['grupo'] for grupo in top_grupos]
    data_vendida = [grupo['total_vendido'] for grupo in top_grupos]
    metas = [1000 if grupo['total_vendido'] >= 1000 else None for grupo in top_grupos]

    return labels, data_vendida, metas
