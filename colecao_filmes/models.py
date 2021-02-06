from django.db import models
from embed_video.fields import EmbedVideoField

class Genero(models.Model):
    nome = models.CharField(max_length = 30, blank = True, null = True)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length = 60, null = True)
    ano = models.IntegerField()
    genero = models.ForeignKey(Genero, related_name='filme', on_delete=models.CASCADE, null = True)
    duração = models.IntegerField()
    sinopse = models.TextField(blank = True, null = True)
    produtora = models.CharField(max_length = 30, blank = True, null = True)
    midia = models.CharField(max_length= 30, blank = True, null = True)
    capa = models.ImageField(blank = True, null = True)
    video = EmbedVideoField(help_text="Copie a URL do vídeo e cole acima.", blank=True)
    
    def __str__(self):
        return self.titulo
