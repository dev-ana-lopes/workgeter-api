from django.db import models

class Candidato(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.IntegerField(unique=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome_completo