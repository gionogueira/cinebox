from django import forms
from .models import Filme, Genero, Profile
from django.contrib.auth.models import User

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'

class GeneroForm(forms.ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['imagem', 'cidade', 'estado', 'idade']