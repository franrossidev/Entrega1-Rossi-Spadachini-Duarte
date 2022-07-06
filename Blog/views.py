from django.shortcuts import redirect, render
from .forms import BusquedaLibro, FormLibro
from .models import Libro
from datetime import datetime
# Create your views here.

def inicio(request):
    return render(request, 'index.html')

def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')

def crear_libro(request):

    if request.method == 'POST':
        form = FormLibro(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data

            fecha = data.get('fecha_creacion')
            
            libro = Libro(
                titulo=data.get('titulo'),
                contenido=data.get('contenido'),
                fecha_creacion=fecha if fecha else datetime.now()
            )
            libro.save()

            #listado_libros = Libro.objects.all()
            
           #return render(request, 'listado_libros.html', {'listado_libros': listado_libros})
            return redirect('listado_libros')
        
        else:
            return render(request, 'crear_libro.html', {'form': form})
            
    form_libro = FormLibro()

    return render(request, 'crear_libro.html', {'form': form_libro})

def listado_libros(request):
    
    nombre_de_busqueda = request.GET.get('titulo')
    
    if nombre_de_busqueda:
        listado_libros = Libro.objects.filter(titulo__icontains=nombre_de_busqueda)
    else:          
        listado_libros = Libro.objects.all()  
    
    form = BusquedaLibro()     
    return render(request, 'listado_libros.html', {'listado_libros': listado_libros, 'form': form})