from django import forms
from ckeditor.fields import RichTextFormField
    
class LibroF(forms.Form):
    titulo=forms.CharField(max_length=30)
    subtitulo=forms.CharField(max_length=30)
    contenido=RichTextFormField()
    fecha_creacion=forms.DateField(required=False)
    imagen=forms.ImageField(required=False)
    autor=forms.CharField(max_length=30)
 
class BusquedaLibro(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
    