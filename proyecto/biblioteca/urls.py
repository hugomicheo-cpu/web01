from django.urls import path
from . import views

urlpatterns = [
    # URLs de Autores
    path("autores/", views.AutorListView.as_view(), name="autor-list"),
    path("autores/<int:pk>/", views.AutorDetailView.as_view(), name="autor-detail"),
    path("autores/nuevo/", views.AutorCreateView.as_view(), name="autor-create"),
    path("autores/<int:pk>/editar/", views.AutorUpdateView.as_view(), name="autor-update"),
    path("autores/<int:pk>/eliminar/", views.AutorDeleteView.as_view(), name="autor-delete"),
    # URLs de Libros
    path("libros/", views.LibroListView.as_view(), name="libro-list"),
    path("libros/<int:pk>/", views.LibroDetailView.as_view(), name="libro-detail"),
    path("libros/nuevo/", views.LibroCreateView.as_view(), name="libro-create"),
    path("libros/<int:pk>/editar/", views.LibroUpdateView.as_view(), name="libro-update"),
    path("libros/<int:pk>/eliminar/", views.LibroDeleteView.as_view(), name="libro-delete"),
    ]