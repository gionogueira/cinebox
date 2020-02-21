from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length = 60, blank = True, null = True)
    ano = models.IntegerField()
    genero = models.CharField(max_length = 30, blank = True, null = True)
    duração = models.IntegerField()
    diretor = models.CharField(max_length = 40, blank = True, null = True)
    produtora = models.CharField(max_length = 30, blank = True, null = True)
    midia = models.CharField(max_length= 30, blank = True, null = True) 
    capa = models.ImageField()

    
    def __str__(self):
        return self.titulo

        
