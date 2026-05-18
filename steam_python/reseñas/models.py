from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import uuid
import os
from django.urls import reverse
from decimal import Decimal


def upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("posts/", filename)


class Juego(models.Model):
    nombre_juego = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to=upload_to)
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_juego}({self.autor})"

    def get_absolute_url(self):
        return reverse("detalle_juego", kwargs={"pk": self.pk})


class Resena(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name="resenas")
    autor = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    cuerpo = models.TextField()
    puntuacion = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(Decimal("0.0")),
            MaxValueValidator(Decimal("5.0")),
        ],
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    @property
    def porcentaje_estrellas(self):
        if self.puntuacion:
            return int(self.puntuacion * 20)
        return 0

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["juego", "autor"], name="una_resena_por_usuario_y_juego"
            )
        ]

    def __str__(self):
        return f"Reseña de {self.autor} para {self.juego.nombre_juego} ({self.puntuacion / 5})"

    def get_absolute_url(self):
        return reverse("detalle_juego", kwargs={"pk": self.pk})
