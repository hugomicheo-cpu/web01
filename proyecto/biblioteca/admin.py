from django.contrib import admin
from .models import Autor, Libro


# Configuración para el modelo Autor
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    # Columnas que se verán en la lista principal
    list_display = ("apellido", "nombre", "nacionalidad")
    # Filtros laterales
    list_filter = ("nacionalidad",)
    # Buscador por nombre y apellido
    search_fields = ("nombre", "apellido")


# Configuración para el modelo Libro
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    # Columnas visibles
    list_display = ("titulo", "autor", "fecha_publicacion", "isbn")
    # Filtro por autor y fecha
    list_filter = ("autor", "fecha_publicacion")
    # Buscador por título e ISBN
    search_fields = ("titulo", "isbn")
    # Permite navegar por fechas de publicación de forma jerárquica
    date_hierarchy = "fecha_publicacion"