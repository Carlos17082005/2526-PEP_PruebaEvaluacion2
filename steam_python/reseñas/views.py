from django.urls import reverse_lazy
from .models import Juego, Resena
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView


class VistaListaJuegos(ListView):
    model = Juego
    template_name = "home.html"
    context_object_name = "juegos"

class VistaDetalleJuego(DetailView):
    model = Juego
    template_name = "detalle_juego.html"

class VistaCrearJuego(CreateView):
    model = Juego
    success_url = reverse_lazy("home")
    template_name = "nuevo_juego.html"
    fields = ["nombre_juego", "imagen","autor"]

class VistaEliminarJuego(DeleteView):
    model = Juego
    template_name = "eliminar_juego.html"
    success_url = reverse_lazy("home")

class VistaEditarJuego(UpdateView):
    model = Juego
    template_name = "editar_juego.html"
    fields = ["nombre_juego", "imagen"]





