from django.shortcuts import render
from .models import Tarifas
from django.http import HttpResponse

# Create your views here.

def viagem(request):
    tarifas = Tarifas.objects.filter(origem="Picuí", destino="Cuité", escalas="1")
    return HttpResponse(tarifas)
    
def passagem(request):
    tarifas = Tarifas.objects.filter(valor__gte="200", valor__lte="500")
    return HttpResponse(tarifas)

def voo(request):
    tarifas = Tarifas.objects.filter(origem="Picuí", destino="Cuité")
    return HttpResponse(tarifas)

def taxa(request):
     tarifas = Tarifas.objects.filter(valor__lt=250)
     return HttpResponse(tarifas)

def tarifabarata(request):
     tarifas = Tarifas.objects.filter()
     return HttpResponse(tarifas)