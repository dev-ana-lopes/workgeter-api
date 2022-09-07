from rest_framework import viewsets,generics
from usuario.models import Candidato, Curriculo, Formulario
from usuario.serializer import CandidatoSerializer, CurriculoSerializer, FormularioSerializer, ListaFormularioCandidatoSerializer


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

class ListaFormularioCandidato(generics.ListAPIView):
    """Listando os formularios de um candidato"""
    def get_queryset(self):
        queryset = Formulario.objects.filter(candidato_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaFormularioCandidatoSerializer
    
     
