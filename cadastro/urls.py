from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('listar_lojas', views.listar_lojas, 
            name='listar_lojas'),
            
    path('incluir_loja', views.incluir_loja,
            name='incluir_loja'),            
]

