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
from django.views.generic.edit import FormMixin
from django.urls import reverse
from .forms import ResenaForm


########################### JUEGOS #######################################################
class VistaListaJuegos(ListView):
    model = Juego
    template_name = "home.html"
    context_object_name = "juegos"

class VistaDetalleJuego(FormMixin, DetailView):
    model = Juego
    template_name = "detalle_juego.html"

    # ****************** Crear Reseña *************************************
    form_class = ResenaForm

    def get_success_url(self):
        # Redirige a esta misma página tras publicar
        return reverse("detalle_juego", kwargs={"pk": self.object.pk})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # Obtenemos el juego actual
        form = self.get_form()
        
        # Validamos el form y que el usuario haya iniciado sesión
        if request.user.is_authenticated and form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        resena = form.save(commit=False) # Pausamos el guardado
        resena.juego = self.object       # Le asignamos el juego actual
        resena.autor = self.request.user # Le asignamos el autor actual
        resena.save()                    # Guardamos definitivamente
        return super().form_valid(form)
    
    # ****************** Crear Reseña *************************************
    
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

########################### RESEÑAS #######################################################
class VistaEliminarResena(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resena
    template_name = "eliminar_resena.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        return (self.get_object().autor == self.request.user) or (self.request.user.is_staff)

    def handle_no_permission(self): 
        messages.error(self.request, "NO tienes permiso para BORRAR este Juego")
        return redirect("detalle_juego", pk=self.get_object().pk)

class VistaEditarResena(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Resena
    template_name = "editar_juego.html"
    fields = ["nombre_juego", "imagen"]

    def test_func(self):
        return (self.get_object().autor == self.request.user) or (self.request.user.is_staff)

    def handle_no_permission(self): 
        messages.error(self.request, "NO tienes permiso para EDITAR este Juego")
        return redirect("detalle_juego", pk=self.get_object().pk)
