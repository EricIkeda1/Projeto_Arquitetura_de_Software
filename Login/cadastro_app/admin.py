from django.contrib import admin
from .models import Produto
from .models import Fabricante  
from .models import Venda, VendaItem
from .models import RedeSocial
# Register your models here.

admin.site.register(Produto)
admin.site.register(Fabricante)

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'data_hora_venda', 'valor_total')

@admin.register(VendaItem)
class VendaItemAdmin(admin.ModelAdmin):
    list_display = ('venda', 'produto', 'quantidade', 'valor_total')
    
admin.site.register(RedeSocial)