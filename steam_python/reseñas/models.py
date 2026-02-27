from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Juego(models.Model):
    nombre_juego = models.CharField(max_length=200)
    imagen = models.TextField()

    def __str__(self):
        return self.nombre_juego


class Resena(models.Model):
    juego = models.ForeignKey(Juego, on_delete=models.CASCADE, related_name="resenas")
    autor = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    cuerpo = models.TextField()
    puntuacion = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )

    def __str__(self):
        return f"Reseña de {self.autor} para {self.juego.nombre_juego} ({self.puntuacion / 10})"
