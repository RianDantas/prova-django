from django.contrib import admin
from .models import Tarifas

# Register your models here.

class TarifasAdmin(admin.ModelAdmin):
    list_display = ('id', 'origem', 'destino', 'escalas', 'valor', 'taxaEmbarque')

admin.site.register(Tarifas, TarifasAdmin)
