from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('listar_lojas', views.listar_lojas, 
            name='listar_lojas'),
            
    path('incluir_loja', views.incluir_loja,
            name='incluir_loja'),   

    path('alterar_loja/<int:codigo>', views.alterar_loja,
            name='alterar_loja'),   

    path('excluir_loja/<int:codigo>', views.excluir_loja,
            name='excluir_loja'),          
]

