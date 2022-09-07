from django.contrib import admin
from django.urls import path, include
from usuario.views import CandidatosViewSet, CurriculosViewSet, FormulariosViewSet, ListaFormularioCandidato
from rest_framework import routers

router = routers.DefaultRouter()
router.register('candidatos', CandidatosViewSet, basename='Candidatos')
router.register('curriculos', CurriculosViewSet, basename='Curriculos')
router.register('formularios', FormulariosViewSet, basename='Formularios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('candidato/<int:pk>/formularios/', ListaFormularioCandidato.as_view())
]
