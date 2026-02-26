from django.shortcuts import render

# Create your views here.
from .models import Reseña


def lista_reseñas(request):
    res = Reseña.objects.all()
    return render(request, "base.html", {"reseñas": res})
