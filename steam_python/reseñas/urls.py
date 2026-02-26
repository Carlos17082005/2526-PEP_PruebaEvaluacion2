# reseñas/urls.py
from django.urls import path
from .views import lista_reseñas

urlpatterns = [
    path("", lista_reseñas, name="base"),
]
