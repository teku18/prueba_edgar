from django import forms
from .models import producto

class productosForm(forms.Form):
    nombre = forms.CharField(max_length=100, label='Nombre del producto'),
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripcion del producto', max_length=200)
