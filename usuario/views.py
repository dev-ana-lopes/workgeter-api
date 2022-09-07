from rest_framework import viewsets,generics
from usuario.models import Candidato, Curriculo, Formulario
from usuario.serializer import CandidatoSerializer, CurriculoSerializer, FormularioSerializer, ListaFormularioCandidatoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class CandidatosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os candidatos"""
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CurriculosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os curriculos"""
    queryset = Curriculo.objects.all()
    serializer_class = CurriculoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class FormulariosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os formularios"""
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaFormularioCandidato(generics.ListAPIView):
    """Listando os formularios de um candidato"""
    def get_queryset(self):
        queryset = Formulario.objects.filter(candidato_id=self.kwargs['pk'])
        return queryset
    
    serializer_class = ListaFormularioCandidatoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
     
