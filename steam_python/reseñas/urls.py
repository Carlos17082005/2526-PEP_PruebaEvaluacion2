# reseñas/urls.py
from django.urls import path
from .views import lista_resenas

urlpatterns = [
    path("", lista_resenas, name="home"),
]
