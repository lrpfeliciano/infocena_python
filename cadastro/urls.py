from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('listar_lojas', views.listar_lojas, 
            name='listar_lojas'),
]

