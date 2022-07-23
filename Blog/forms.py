from django import forms
    
class BusquedaLibro(forms.Form):
    titulo = forms.CharField(max_length=30, required=False)
    