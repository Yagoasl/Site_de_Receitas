from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class LivroReceitas(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_receita = models.CharField(max_length=80)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_de_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    publicada = models.BooleanField(default=False)


