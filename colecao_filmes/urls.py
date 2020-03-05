from django.urls import path
from . import views
from colecao_filmes.views import CadastroFilme 

urlpatterns = [
    path('', CadastroFilme.as_view(), name='cadastrofilme'),
    path('colecaofilmes/', views.colecaofilmes, name='colecaofilmes'),
    path('editarfilme/<int:pk>/', views.editarfilme, name='editarfilme'),
    path('deletarfilme/<int:pk>/', views.deletarfilme, name='deletarfilme'),
]