from django.contrib import admin
from tinder.models import Candidato

class Candidatos(admin.ModelAdmin):
    list_display = ('id', 'nome_completo', 'cpf', 'celular', 'email', 'password')
    list_display_links = ('id', 'nome_completo', 'cpf')
    search_fields = ('nome_completo', )
    list_per_page = 10
  
admin.site.register(Candidato, Candidatos)
