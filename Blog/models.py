from django.db import models

# Create your models here.

class Libro(models.Model):
    titulo=models.CharField(max_length=30)
    contenido=models.CharField(max_length=3000)
    fecha_creacion=models.DateField(null=True)
    
    def __str__(self):
        return f'Titulo: {self.titulo} - Descripcion: {self.contenido}'