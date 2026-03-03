from django.contrib import admin

# Register your models here.
from .models import Resena, Juego

class JuegoAdmin(admin.ModelAdmin): 
    list_display = ("nombre_juego","autor","imagen")


admin.site.register(Resena)
admin.site.register(Juego ,JuegoAdmin)
