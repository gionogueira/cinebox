from django.shortcuts import render
from django.shortcuts import redirect
from .models import Filme
from .forms import FilmeForm
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def index(request):
    filme = Filme.objects.all()
    return render(request, 'colecaofilmes/index.html', {'filme': filme})

class CadastroFilme(View):
    def get(self, request):
        form = FilmeForm
        return render(request, 'colecaofilmes/cadastrofilme.html', {'form': form})

    def post(self, request):
        form = FilmeForm(request.POST, request.FILES)
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

    if request.method == 'POST':
        form = FilmeForm(request.POST, request.FILES, instance=filme)

        if form.is_valid():
            form.save()
            return redirect('colecaofilmes')
    else:
        form = FilmeForm(instance=filme)
    
    return render(request, 'colecaofilmes/cadastrofilme.html', {'form': form}) 

def deletarfilme(request, pk):
    filme = Filme.objects.get(pk=pk)
    filme.delete()
    return redirect('colecaofilmes')

class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    