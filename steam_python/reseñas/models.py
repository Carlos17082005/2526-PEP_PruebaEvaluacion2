from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Reseña(models.Model):
    nombre_juego = models.CharField(max_length=200)
    autor = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE,
    )
    cuerpo = models.TextField()
    puntuacion = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(50)]
    )


def __str__(self):
    return self.nombre_juego
