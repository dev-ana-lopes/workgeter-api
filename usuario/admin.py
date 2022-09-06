from django.contrib import admin
from usuario.models import Candidato, Curriculo, Formulario

class Candidatos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idade', 'email')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', )
    list_per_page = 20

class Curriculos(admin.ModelAdmin):
    list_display = ('id', 'experiencia', 'formacao')
    list_display_links = ('id', 'experiencia')
    search_fields = ('id', )
    list_per_page = 20
    
class Formularios(admin.ModelAdmin):
    list_display = ('id', 'candidato', 'curriculo', 'data')
    list_display_links = ('id', 'candidato')
    search_fields = ('id', )
    list_per_page = 20

    
admin.site.register(Candidato, Candidatos)
admin.site.register(Curriculo, Curriculos)
admin.site.register(Formulario, Formularios)
    
