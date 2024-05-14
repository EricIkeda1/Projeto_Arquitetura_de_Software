from django.shortcuts import render
# Create your views here.

def login_view(request):
    return render(request, 'Login.html')

def register_view(request):
    return render(request, 'Cadastro.html')

def tela_de_graficos(request):
    return render(request, 'Tela_de_graficos.html')
