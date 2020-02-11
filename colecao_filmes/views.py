from django.shortcuts import render

def cadastro_filme(request):
    return render(request, 'colecaofilmes/colecaofilmes.html', {}) 
