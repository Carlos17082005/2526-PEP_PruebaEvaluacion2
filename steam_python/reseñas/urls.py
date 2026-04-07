# reseñas/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (VistaListaJuegos,
                    VistaDetalleJuego,
                    VistaCrearJuego,
                    VistaEliminarJuego,
                    VistaEditarJuego,
                    VistaEditarResena,
                    VistaEliminarResena)

urlpatterns = [
    # ************* Reseñas **********************
    path("", VistaListaJuegos.as_view(), name="home"),
    path("juego/nuevo/", VistaCrearJuego.as_view(), name="nuevo_juego"),
    path("juego/detalle/<int:pk>", VistaDetalleJuego.as_view(), name="detalle_juego"),
    path("juego/eliminar/<int:pk>", VistaEliminarJuego.as_view(), name="eliminar_juego"),
    path("juego/editar/<int:pk>", VistaEditarJuego.as_view(), name="editar_juego"),
    # ************* Reseñas **********************
    path("resena/eliminar/<int:pk>", VistaEliminarResena.as_view(), name="eliminar_resena"),
    path("resena/editar/<int:pk>", VistaEditarResena.as_view(), name="editar_resena"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)