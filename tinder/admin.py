from django.contrib import admin
from tinder.models import Candidato, Empresa, Formulario, Vaga

class Candidatos(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'celular', 'email', 'password')
    list_display_links = ('id', 'nome_completo', 'cpf')
    search_fields = ('cpf', )
    list_per_page = 10
  
admin.site.register(Candidato, Candidatos)

class Empresas(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'cnpj', 'celular_empresa', 'email_empresa', 'senha_empresa')
    list_display_links = ('id', 'razao_social', 'cnpj')
    search_fields = ('cnpj', )
    list_per_page = 10
  
admin.site.register(Empresa, Empresas)

class Formularios(admin.ModelAdmin):
    list_display = ('id', 'endereco', 'escolaridade', 'experiencia', 'projetos', 'cursos', 'idiomas', 'valores_pessoais', 'descricao_participacao', 'descricao_valores_empresa', 'portfolio')
    list_display_links = ('id', 'endereco')
    search_fields = ('endereco', )
    list_per_page = 10
  
admin.site.register(Formulario, Formularios)

class Vagas(admin.ModelAdmin):
    list_display = ('id', 'atividade_vagas', 'requisitos_vagas', 'beneficios_vagas', 'valores_vagas', 'descricao_participacao_vagas')
    list_display_links = ('id', 'atividade_vagas', 'requisitos_vagas')
    search_fields = ('requisitos_vagas', )
    list_per_page = 10
  
admin.site.register(Vaga, Vagas)

