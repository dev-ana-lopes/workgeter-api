from django.contrib import admin
from django.urls import path, include
from usuario.views import CandidatosViewSet
#from empresa.views import CandidatosViewSet, CurriculosViewSet, FormulariosViewSet, ListaFormularioCandidato
from rest_framework import routers

router = routers.DefaultRouter()
router.register('candidatos', CandidatosViewSet, basename='Candidatos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
