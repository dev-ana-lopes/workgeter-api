from django.contrib import admin
from tinder.models import Candidato, Empresa, Formulario

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
    list_display_links = ('id')
    search_fields = ('id', )
    list_per_page = 10
  
admin.site.register(Formulario, Formularios)










