from django import forms
from .models import Produto
from .models import Fabricante
from .models import Grupo, Subgrupo
from django import forms
from .models import Feedback


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco_custo', 'preco_venda', 'peso', 'quantidade_comprado', 'quantidade_vendido', 'fabricante', 'grupo', 'subgrupo']
        widgets = {
            'preco_custo': forms.TextInput(attrs={'type': 'number', 'step': '0.01', 'min': '0', 'class': 'form-control', 'placeholder': 'Preço de custo em R$'}),
            'preco_venda': forms.TextInput(attrs={'type': 'number', 'step': '0.01', 'min': '0', 'class': 'form-control', 'placeholder': 'Preço de venda em R$'}),
        }

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = '__all__'  
        
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nome', 'descricao']

class SubgrupoForm(forms.ModelForm):
    class Meta:
        model = Subgrupo
        fields = ['grupo', 'nome', 'descricao']
        
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
