from django.shortcuts import render
from .models import Juego, Resena
from django.views.generic import ListView, DetailView, CreateView


class VistaListaJuegos(ListView):
    model = Juego
    template_name = "home.html"
    context_object_name = "juegos"

class VistaDetalleJuego(DetailView):
    model = Juego
    template_name = "detalle_juego.html"

    # Le decimos a Django: "Busca en la columna 'nombre_juego' de la base de datos..."
    slug_field = "nombre_juego" 
    # "...el valor que te llega desde la URL llamado también 'nombre_juego'"
    slug_url_kwarg = "nombre_juego"

class VistaCrearJuego(CreateView):
    model = Juego
    template_name = "juego_post.html"
    fields = ["nombre_juego", "imagen"]