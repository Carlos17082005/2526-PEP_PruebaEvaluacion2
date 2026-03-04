from django.contrib import admin

# Register your models here.
from .models import Resena, Juego

class JuegoAdmin(admin.ModelAdmin): 
    list_display = ("nombre_juego","autor","imagen")

class ResenaAdmin(admin.ModelAdmin): 
    list_display = ("autor","puntuacion","cuerpo","juego")

admin.site.register(Resena, ResenaAdmin)
admin.site.register(Juego, JuegoAdmin)
