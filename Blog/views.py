from django.shortcuts import redirect, render
from .forms import BusquedaLibro
from .models import Libro
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def inicio(request):
    return render(request, 'index.html')

@login_required
def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

class ListadoLibros(ListView):
    model=Libro
    template_name = 'listado_libros.html'

    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo: 
            object_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            object_list = self.model.objects.all()
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = BusquedaLibro()
        return context
    
    
class CrearLibro(LoginRequiredMixin, CreateView):
    model=Libro
    template_name = 'crear_libro.html'
    success_url = '/libros'
    fields = ['titulo', 'contenido', 'fecha_creacion']
    
class EditarLibro(LoginRequiredMixin, UpdateView):
    model=Libro
    template_name = 'editar_libro.html'
    success_url = '/libros'
    fields = ['titulo', 'contenido', 'fecha_creacion']


class EliminarLibro(LoginRequiredMixin, DeleteView):
    model=Libro
    template_name = 'eliminar_libro.html'
    success_url = '/libros'


class MostrarLibro(DetailView):
    model = Libro
    template_name = 'mostrar_libro.html'