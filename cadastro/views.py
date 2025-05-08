from django.http import HttpResponse
from django.shortcuts import redirect, render

from cadastro.forms import LojaForm
from .models import Loja
from django.contrib import messages
from django.db.models.functions import Lower

# Create your views here.

def index(request):
    return HttpResponse("Olá Mundo! Agora é web")

def listar_lojas(request):
    lojas = Loja.objects.order_by(Lower('nome'))
    return render(request, 'listar_lojas.html',
                  {'lojas':lojas })

def incluir_loja(request):
    if request.method == 'POST':
        form = LojaForm(request.POST)
        if form.is_valid():
            form.save()
            return listar_lojas(request)
            # msg = 'Registro cadastrado com sucesso'
            # return render(request, 'incluir_loja.html',
            #         {'mensagem': msg, 'formulario': form})
    form = LojaForm()
    return render(request, 'incluir_loja.html',
                  {'formulario': form})

def alterar_loja(request, codigo):
    loja = Loja.objects.get(id=codigo)

    if request.method == 'POST':
        form = LojaForm(request.POST, instance=loja)
        if form.is_valid():
            form.save()
            return redirect('listar_lojas')
    form = LojaForm(instance=loja)
    return render(request, 'incluir_loja.html',
                  {'formulario': form})

def excluir_loja(request, codigo):
    loja = Loja.objects.get(id=codigo)

    Loja.delete(loja)

    return redirect('listar_lojas')

