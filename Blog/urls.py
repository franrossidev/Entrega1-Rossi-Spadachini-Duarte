from django.urls import path
from .views import inicio, sobre_nosotros
from . import views

urlpatterns = [
    path('', inicio, name='index'),
    path('about/', sobre_nosotros, name='sobre_nosotros'),
    path('crear-libro/', views.CrearLibro.as_view(), name='crear_libro'),
    path('libros/', views.ListadoLibros.as_view(), name='listado_libros'),
    path('editar-libro/<int:pk>/', views.EditarLibro.as_view(), name='editar_libro'),
    path('eliminar-libro/<int:pk>/', views.EliminarLibro.as_view(), name='eliminar_libro'),
    path('mostrar-libro/<int:pk>/', views.MostrarLibro.as_view(), name='mostrar_libro'),
]