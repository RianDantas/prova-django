from django.urls import path
from . import views

urlpatterns = [
    path("viagem/", views.viagem),
    path("passagem/", views.passagem),
    path("voo/", views.voo),
    path("taxa/", views.taxa),
    path("tarifabarata/", views.tarifabarata),

    
]