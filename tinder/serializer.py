from rest_framework import serializers
from tinder.models import Candidato, Empresa

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = ['id', 'nome_completo', 'cpf', 'celular', 'email', 'password']



class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'