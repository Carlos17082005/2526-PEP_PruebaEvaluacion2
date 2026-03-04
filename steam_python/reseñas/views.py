from django.urls import reverse_lazy
from .models import Juego, Resena
from django.views.generic import (ListView, 
                                  DetailView, 
                                  CreateView, 
                                  UpdateView, 
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.shortcuts import redirect

class VistaListaJuegos(ListView):
    model = Juego
    template_name = "home.html"
    context_object_name = "juegos"

class VistaDetalleJuego(DetailView):
    model = Juego
    template_name = "detalle_juego.html"

class VistaCrearJuego(LoginRequiredMixin, CreateView):
    model = Juego
    success_url = reverse_lazy("home")
    template_name = "nuevo_juego.html"
    fields = ["nombre_juego", "imagen","autor"]

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class VistaEliminarJuego(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Juego
    template_name = "eliminar_juego.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return (self.get_object().autor == self.request.user) or (self.request.user.is_staff)

    def handle_no_permission(self): 
        messages.error(self.request, "NO tienes permiso para BORRAR este Juego")
        return redirect("detalle_juego", pk=self.get_object().pk)

class VistaEditarJuego(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Juego
    template_name = "editar_juego.html"
    fields = ["nombre_juego", "imagen"]

    def test_func(self):
        return (self.get_object().autor == self.request.user) or (self.request.user.is_staff)

    def handle_no_permission(self): 
        messages.error(self.request, "NO tienes permiso para EDITAR este Juego")
        return redirect("detalle_juego", pk=self.get_object().pk)



