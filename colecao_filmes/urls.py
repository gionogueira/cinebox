from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastrofilme, name='cadastrofilme'),
    path('colecaofilmes/', views.colecaofilmes, name='colecaofilmes'),
]