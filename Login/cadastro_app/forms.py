from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco_custo', 'preco_venda', 'peso', 'quantidade_comprado', 'quantidade_vendido', 'fabricante', 'grupo', 'subgrupo']
