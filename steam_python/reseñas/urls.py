# reseñas/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import VistaListaJuegos, VistaDetalleJuego, VistaCrearJuego

urlpatterns = [
    path("", VistaListaJuegos.as_view(), name="home"),
    path("juego/<str:nombre_juego>/", VistaDetalleJuego.as_view(), name="detalle_juego"),
    path("juego/nuevo/", VistaCrearJuego.as_view(), name="nuevo_juego"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)