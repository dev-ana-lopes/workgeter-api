from django.db import models

class Candidato(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Curriculo(models.Model):
    experiencia = models.CharField(max_length=50)
    formacao = models.CharField(max_length=50)
    
    def __str__(self):
        return self.formacao
    
class Formulario(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    curriculo = models.ForeignKey(Curriculo, on_delete=models.CASCADE)
    data = models.DateField() 