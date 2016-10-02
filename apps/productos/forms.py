from django import forms
from django.forms import Textarea
from .models import producto

class productosForm(forms.ModelForm):

    class Meta:
        model=producto

        fields=['nombre', 'descripcion']

        widgets={
            'descripcion': Textarea(attrs={'cols':50,'rows':10}),

        }
