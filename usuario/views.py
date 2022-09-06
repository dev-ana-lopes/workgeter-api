from rest_framework import viewsets
from usuario.models import Candidato, Curriculo, Formulario
from usuario.serializer import CandidatoSerializer, CurriculoSerializer, FormularioSerializer

class CandidatosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os candidatos"""
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class CurriculosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os curriculos"""
    queryset = Curriculo.objects.all()
    serializer_class = CurriculoSerializer
    
class FormulariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os formularios"""
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer



