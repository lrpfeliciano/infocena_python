from django.http import HttpResponse
from django.shortcuts import render

from cadastro.forms import LojaForm
from .models import Loja

# Create your views here.

def index(request):
    return HttpResponse("Olá Mundo! Agora é web")

def listar_lojas(request):
    lojas = Loja.objects.order_by('nome')
    return render(request, 'listar_lojas.html',
                  {'lojas':lojas })

def incluir_loja(request):
    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():
            form.save()
            return listar_lojas(request)
    form = LojaForm()
    return render(request, 'incluir_loja.html',
                  {'formulario': form})

