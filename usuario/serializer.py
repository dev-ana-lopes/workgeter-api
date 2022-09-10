from rest_framework import serializers
from usuario.models import Candidato

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ['id', 'nome_completo', 'cpf', 'celular', 'email', 'password']
        

        

        