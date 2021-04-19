from django.shortcuts import render, redirect
from .models import Filme, Genero, Profile
from .forms import FilmeForm
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# from googletrans import Translator
# import time

def index(request):
    return render(request, 'colecaofilmes/index.html', {})

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

class ColecaoFilmes(View):
    def get(self, request):
        genero = Genero.objects.all()
        filme = Filme.objects.filter(genero__in=genero)
        context = {
        'filme': filme,
        'genero': genero
        }
        return render(request, 'colecaofilmes/colecaofilmes.html', context)

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

def detalharfilme(request, pk):
    filme = Filme.objects.get(pk=pk)
    return render(request, 'colecaofilmes/detalharfilme.html', {'filme': filme})

def deletarfilme(request, pk):
    filme = Filme.objects.get(pk=pk)
    filme.delete()
    return redirect('colecaofilmes')    

class register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def profile(request):
    profile = Profile.objects.all()
    filme = Filme.objects.all()
    context = {
        'profile': profile,
        'filme': filme
    }
    return render(request, 'colecaofilmes/perfil.html', context)



