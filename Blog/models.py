from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Libro(models.Model):
    titulo=models.CharField(max_length=30)
    subtitulo=models.CharField(max_length=30, null=True)
    contenido=RichTextField(null=True)
    fecha_creacion=models.DateField(auto_now_add=True, null=True , blank=True)
    imagen=models.ImageField(upload_to='imagenes', null=True, blank=True)
    autor=models.CharField(max_length=30, null=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo} - Fecha creacion: {self.fecha_creacion} - Creado por {self.autor}' 