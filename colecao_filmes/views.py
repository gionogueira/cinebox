from django.shortcuts import render
from django.shortcuts import redirect
from .models import Filme
from .forms import FilmeForm
from django.views.generic import View

class CadastroFilme(View):
    def get(self, request):
        form = FilmeForm
        return render(request, 'colecaofilmes/cadastrofilme.html', {'form': form})

    def post(self, request):
        form = FilmeForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('colecaofilmes')
        else:
            print(form.errors) 

        return render(request, 'colecaofilmes/cadastrofilme.html', {'form': form})             

def colecaofilmes(request):
    filme = Filme.objects.all()
    return render(request, 'colecaofilmes/colecaofilmes.html', {'filme': filme})

def editarfilme(request, pk):
    filme = Filme.objects.get(pk=pk)
    form = FilmeForm(request.POST or None, instance=filme)

    if form.is_valid():
        form.save()
        return redirect('colecaofilmes')
    else:
        print(form.errors) 
    
    return render(request, 'colecaofilmes/cadastrofilme.html', {'form': form}) 

def deletarfilme(request, pk):
    filme = Filme.objects.get(pk=pk)
    filme.delete()
    return redirect('colecaofilmes')
    