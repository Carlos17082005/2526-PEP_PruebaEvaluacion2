from django.contrib import admin

# Register your models here.
from .models import Resena, Juego

admin.site.register(Resena)
admin.site.register(Juego)
