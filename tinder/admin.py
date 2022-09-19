from django.contrib import admin
from tinder.models import Candidato, Empresa

class Candidatos(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'celular', 'email', 'password')
    list_display_links = ('id', 'nome_completo', 'cpf')
    search_fields = ('nome_completo', )
    list_per_page = 10
  
admin.site.register(Candidato, Candidatos)

class Empresas(admin.ModelAdmin):
    list_display = ('id', 'razao_social', 'cnpj', 'celular_empresa', 'email_empresa', 'senha_empresa')
    list_display_links = ('id', 'razao_social', 'cnpj')
    search_fields = ('razao_social', )
    list_per_page = 10
  
admin.site.register(Empresa, Empresas)
