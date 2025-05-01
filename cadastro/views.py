from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Olá Mundo! Agora é web")

def listar_lojas(request):
    return render(request, 'listar_lojas.html')

