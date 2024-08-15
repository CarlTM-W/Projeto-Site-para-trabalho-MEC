from django.db import models

class TipoCorreia(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='tipos_correia/')

    def __str__(self):
        return self.nome

class Formula(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='formulas/')

    def __str__(self):
        return self.nome
