from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Autor, Libro

# --- VISTAS PARA AUTOR ---


class AutorListView(ListView):
    model = Autor
    template_name = "biblioteca/autor_list.html"
    context_object_name = "autores"


class AutorDetailView(DetailView):
    model = Autor
    template_name = "biblioteca/autor_detail.html"


class AutorCreateView(CreateView):
    model = Autor
    fields = ["nombre", "apellido", "nacionalidad", "fecha_nacimiento"]
    template_name = "biblioteca/autor_form.html"
    success_url = reverse_lazy("autor-list")


class AutorUpdateView(UpdateView):
    model = Autor
    fields = ["nombre", "apellido", "nacionalidad", "fecha_nacimiento"]
    template_name = "biblioteca/autor_form.html"
    success_url = reverse_lazy("autor-list")


class AutorDeleteView(DeleteView):
    model = Autor
    template_name = "biblioteca/autor_confirm_delete.html"
    success_url = reverse_lazy("autor-list")


# --- VISTAS PARA LIBRO ---


class LibroListView(ListView):
    model = Libro
    template_name = "biblioteca/libro_list.html"
    context_object_name = "libros"


class LibroDetailView(DetailView):
    model = Libro
    template_name = "biblioteca/libro_detail.html"


class LibroCreateView(CreateView):
    model = Libro
    fields = ["titulo", "isbn", "fecha_publicacion", "autor", "resumen", "paginas"]
    template_name = "biblioteca/libro_form.html"
    success_url = reverse_lazy("libro-list")


class LibroUpdateView(UpdateView):
    model = Libro
    fields = ["titulo", "isbn", "fecha_publicacion", "autor", "resumen", "paginas"]
    template_name = "biblioteca/libro_form.html"
    success_url = reverse_lazy("libro-list")


class LibroDeleteView(DeleteView):
    model = Libro
    template_name = "biblioteca/libro_confirm_delete.html"
    success_url = reverse_lazy("libro-list")