from rest_framework import serializers
from usuario.models import Candidato, Curriculo, Formulario

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ['id', 'nome', 'idade', 'email']
        
class CurriculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curriculo
        fields = ['id', 'experiencia', 'formacao']
        
class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        ##fields = ['id', 'candidato', 'curriculo', 'data']
        exclude = []
        
class ListaFormularioCandidatoSerializer(serializers.ModelSerializer):
    
    candidato = serializers.ReadOnlyField(source='candidato.nome')
    curriculo = serializers.ReadOnlyField(source='curriculo.experiencia')
    
    class Meta:
        model = Formulario
        fields = ['candidato', 'curriculo']

        

        