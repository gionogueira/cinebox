from django.shortcuts import render
from .models import Filme

def cadastrofilme(request):
    return render(request, 'colecaofilmes/cadastrofilme.html', {})

def colecaofilmes(request):
    filme = Filme.objects.all()
    return render(request, 'colecaofilmes/colecaofilmes.html', {'filme': filme})      

