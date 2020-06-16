from django import forms
from .models import Filme, Genero

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'