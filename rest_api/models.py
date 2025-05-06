from django.db import models

class Categoria(models.Model):
    nombre = models.CharField("Nombre de categoría", max_length=100, unique=True)

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

class Juego(models.Model):
    categoria       = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="juegos",
        verbose_name="Categoría"
    )
    nombre          = models.CharField("Nombre del juego", max_length=200)
    precio_original = models.DecimalField("Precio original", max_digits=10, decimal_places=2)
    precio_oferta   = models.DecimalField(
        "Precio con oferta",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Si no hay oferta, dejar vacío"
    )
    descripcion      = models.TextField("Descripción")
    ruta_imagen      = models.CharField("Ruta de imagen", max_length=255)

    class Meta:
        verbose_name = "Juego"
        verbose_name_plural = "Juegos"
        ordering = ["nombre"]

    def __str__(self):
        return f"{self.nombre} ({self.categoria.nombre})"
