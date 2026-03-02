# reseñas/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import VistaListaJuegos, VistaDetalleJuego, VistaCrearJuego, VistaEliminarJuego

urlpatterns = [
    path("", VistaListaJuegos.as_view(), name="home"),
    path("juego/detalle/<str:nombre_juego>/", VistaDetalleJuego.as_view(), name="detalle_juego"),
    path("juego/nuevo/", VistaCrearJuego.as_view(), name="nuevo_juego"),
    path("juego/eliminar/", VistaEliminarJuego.as_view(), name="eliminar_juego"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)