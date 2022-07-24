from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Libro(models.Model):
    titulo=models.CharField(max_length=30)
    contenido=RichTextField(null=True)
    fecha_creacion=models.DateField(null=True)
    #imagen=models.ImageField(upload_to='libros', null=True, blank=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo} - Descripcion: {self.contenido}'