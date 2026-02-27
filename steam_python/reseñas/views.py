from django.shortcuts import render

# Create your views here.
from .models import Juego, Resena 


def lista_resenas(request):
    res = Resena.objects.all()
    return render(request, "base.html", {"resenas": res})
