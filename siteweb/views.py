from django.shortcuts import render

from cadastro.models import Produto
from django.db.models.functions import Lower

# Create your views here.
def produtos(request):
    produtos = Produto.objects.order_by(Lower('nome'))
    return render(request, 'produtos.html', 
                  {'produtos': produtos})

def index(request):
    return render(request, 'index.html')

def quem_somos(request):
    return render(request, 'quem_somos.html')

