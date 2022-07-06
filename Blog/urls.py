from django.urls import path
from .views import inicio, listado_libros, sobre_nosotros, crear_libro
urlpatterns = [
    path('', inicio, name='index'),
    path('about/', sobre_nosotros, name='sobre_nosotros'),
    path('crear-libro/', crear_libro, name='crear_libro'),
    path('libros/', listado_libros, name='listado_libros'),
]