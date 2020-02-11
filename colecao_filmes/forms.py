from django import forms
from .models import FilmeAssistido

class FilmeAssistidoForm(forms.ModelForm):
    class Meta:
        model = FilmeAssistido
        fields = ('titulo', 'ano', 'genero', 'duração', 'diretor', 'produtora', 'midia', 'capa')