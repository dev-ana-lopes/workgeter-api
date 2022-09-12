from rest_framework import viewsets #generics
from tinder.models import Candidato
from tinder.serializer import CandidatoSerializer
#from rest_framework.authentication import BasicAuthentication
#from rest_framework.permissions import IsAuthenticated

class CandidatosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os candidatos"""
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    """authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]"""

     