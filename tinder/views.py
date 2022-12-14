from rest_framework import viewsets #generics
from tinder.models import Candidato, Empresa, Formulario, Vaga
from tinder.serializer import CandidatoSerializer, EmpresaSerializer, FormularioSerializer, VagaSerializer

#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

class CandidatosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os candidatos"""
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    """authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]"""

class EmpresaViewSet(viewsets.ModelViewSet):
    """Exibindo todas empresas"""
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class FormularioViewSet(viewsets.ModelViewSet):
    """Exibindo todos formulários"""
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer

class VagaViewSet(viewsets.ModelViewSet):
    """Exibindo todas empresas"""
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer
