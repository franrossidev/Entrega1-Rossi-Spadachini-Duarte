from django import forms

class FormLibro(forms.Form):
    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=3000)
    fecha_creacion = forms.DateField(required=False)
    
class BusquedaLibro(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)