from django.db import models

class Candidato(models.Model):
    
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    celular = models.CharField(max_length=11)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.cpf
    

class Empresa(models.Model):
    
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14, unique=True)
    celular_empresa = models.CharField(max_length=11, unique=True)
    email_empresa = models.CharField(max_length=50)
    senha_empresa = models.CharField(max_length=20)
    
    def __str__(self):
        return self.cnpj


class Formulario(models.Model):

   ## candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, default=True)
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
        return self.endereco

class Vaga(models.Model):
    
   ## empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, default=True)
    atividade_vagas = models.CharField(max_length=1000)
    requisitos_vagas = models.CharField(max_length=1000)
    beneficios_vagas = models.CharField(max_length=1000)
    valores_vagas = models.CharField(max_length=500)
    descricao_participacao_vagas = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.atividade_vagas