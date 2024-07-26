from django.db import models

# Create your models here.

class Tarifas(models.Model):
    origem = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    escalas = models.IntegerField(default=0)
    valor = models.IntegerField(default=0)
    taxaEmbarque = models.IntegerField(default=0)

    def __str__(self):
        return self.origem + self.destino + str(self.valor)
