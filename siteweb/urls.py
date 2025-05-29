
from django.urls import path

from siteweb import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quem_somos', views.quem_somos,
         name='quem_somos'),
    path('produtos', views.produtos,
         name='produtos'), 
   
]