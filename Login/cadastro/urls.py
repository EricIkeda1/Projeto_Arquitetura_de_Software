"""
URL configuration for cadastro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cadastro_app import views
from cadastro_app.views import login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='index'),  # Rota para a raiz do projeto
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('graficos/', views.graficos, name='graficos'),
    path('inicio/', views.inicio, name='inicio'),
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'),
    path('listar/', views.listar_produtos, name='listar_produtos'),
    path('acesso-negado/', views.acesso_negado, name='acesso_negado'),
    path('fabricante/', views.cadastrar_fabricante, name='cadastro_fabricante'),
    path('pagina-sucesso/', views.pagina_sucesso, name='pagina_sucesso'),
    path('listar_grupos/', views.listar_grupos, name='listar_grupos'),
    path('adicionar_grupos/', views.adicionar_grupo, name='adicionar_grupo'),
    path('subgrupos/', views.adicionar_subgrupo, name='adicionar_subgrupo'),
    path('remover/<int:id>/', views.remover_produto, name='remover_produto'),
    path('venda/adicionar/', views.adicionar_venda, name='adicionar_venda'),
    path('venda/<int:venda_id>/', views.venda_detalhe, name='venda_detalhe'),
]

