from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    fecha_publicacion = models.DateField()
    # Relación: Un autor tiene muchos libros
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    resumen = models.TextField(max_length=1000, help_text="Breve descripción del libro")

    def __str__(self):
        return self.titulo