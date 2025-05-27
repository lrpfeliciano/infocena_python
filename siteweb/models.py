from django.db import models

# Create your models here.
class MotivoContato(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return self.nome
    
class FaleConosco(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    motivoContato = models.ForeignKey(MotivoContato,
                            on_delete=models.DO_NOTHING)
