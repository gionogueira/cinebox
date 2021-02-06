from django.shortcuts import render, redirect
from .models import Filme, Genero
from .forms import FilmeForm
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
# from googletrans import Translator
# import time

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

class ColecaoFilmes(View):
    def get(self, request):
        genero = Genero.objects.all()
        filme = Filme.objects.filter(genero__in=genero)
        context = {
        'filme': filme,
        'genero': genero
        }
        print(context)
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

# def iniciar():
#     urls = ["translate.google.com", "translate.google.com.ar", "translate.google.com.br",
#     "translate.google.com"];
#     user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
#     return Translator(service_urls=urls, user_agent=user, raise_exception=False, timeout= None)

# def traduzir(frases):
#     for i in range(100):
#         try:
#             buffer = iniciar().translate(frases, dest='pt')
#             return buffer
#         except:
#             time.sleep(2)

# frases = ["What's my user agent?", "Sorry, we get too much bot/crawler traffic from hosting companies so now we just block it outright. Our API provides you all the same information and makes it easier for you, instead of having to scrape the HTML."]
# retornos = traduzir( frases )
# for retorno in retornos:
#     print(retorno.text)
