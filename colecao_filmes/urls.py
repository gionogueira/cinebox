from django.urls import path
from . import views
from colecao_filmes.views import CadastroFilme
from colecao_filmes.views import ColecaoFilmes 
from colecao_filmes.views import register
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrofilme/', CadastroFilme.as_view(), name='cadastrofilme'),
    path('colecaofilmes/', ColecaoFilmes.as_view(), name='colecaofilmes'),
    path('editarfilme/<int:pk>/', views.editarfilme, name='editarfilme'),
    path('deletarfilme/<int:pk>/', views.deletarfilme, name='deletarfilme'),
    path('registrar/', views.register.as_view(), name='registrar'),
    path('detalharfilme/<int:pk>/', views.detalharfilme, name='detalharfilme'),
    path('perfil/', views.profile, name='profile'),
]