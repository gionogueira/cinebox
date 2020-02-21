from django.shortcuts import render

def cadastrofilme(request):
    return render(request, 'colecaofilmes/cadastrofilme.html', {})

def colecaofilmes(request):
    return render(request, 'colecaofilmes/colecaofilmes.html', {})      

