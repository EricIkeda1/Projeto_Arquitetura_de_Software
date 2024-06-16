from django.db import models
from django.utils import timezone

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco_custo = models.DecimalField(max_digits=10, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_comprado = models.IntegerField()
    quantidade_vendido = models.IntegerField(default=0)
    fabricante = models.CharField(max_length=255)
    grupo = models.CharField(max_length=255)
    subgrupo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    
class Fabricante(models.Model):
    nome_fabricante = models.CharField(max_length=100)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    vendedor = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome_fabricante

class Grupo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Subgrupo(models.Model):
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Venda(models.Model):
    data_hora_venda = models.DateTimeField(default=timezone.now)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Venda #{self.id} - {self.data_hora_venda}"

class VendaItem(models.Model):
    venda = models.ForeignKey(Venda, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        # Atualiza o estoque ao salvar
        self.produto.quantidade_vendido += self.quantidade
        self.produto.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"
    
class RedeSocial(models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.nome
