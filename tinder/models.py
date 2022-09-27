from django.db import models

class Candidato(models.Model):
    
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.CharField(max_length=11, unique=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.cpf


class Empresa(models.Model):
    
    razao_social = models.CharField(max_length=255, unique=True)
    cnpj = models.CharField(max_length=14, unique=True)
    celular_empresa = models.CharField(max_length=11, unique=True)
    email_empresa = models.CharField(max_length=50)
    senha_empresa = models.CharField(max_length=20)
    
    def __str__(self):
        return self.cnpj


class Formulario(models.Model):
    
    Candidato
    endereco = models.CharField(max_length=255)
    escolaridade = models.CharField(max_length=100)
    experiencia = models.CharField(max_length=255)
    projetos = models.CharField(max_length=255)
    cursos = models.CharField(max_length=255)
    idiomas = models.CharField(max_length=255)
    valores_pessoais = models.CharField(max_length=255)
    descricao_participacao = models.CharField(max_length=255)
    descricao_valores_empresa = models.CharField(max_length=255)
    portfolio = models.CharField(max_length=255)
    
    def __str__(self):
        return Candidato