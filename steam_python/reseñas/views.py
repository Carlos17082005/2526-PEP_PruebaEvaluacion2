from django.shortcuts import render

# Create your views here.
from .models import Juego, Resena
from django.views.generic import ListView


class VistaListaJuegos(ListView):
    model = Juego
    template_name = "home.html"
    context_object_name = "juegos"