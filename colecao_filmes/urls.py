from django.urls import path
from . import views
from colecao_filmes.views import CadastroFilme 
from colecao_filmes.views import register
urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrofilme/', CadastroFilme.as_view(), name='cadastrofilme'),
    path('colecaofilmes/', views.colecaofilmes, name='colecaofilmes'),
    path('editarfilme/<int:pk>/', views.editarfilme, name='editarfilme'),
    path('deletarfilme/<int:pk>/', views.deletarfilme, name='deletarfilme'),
    path('registrar/', views.register.as_view(), name='registrar')
]