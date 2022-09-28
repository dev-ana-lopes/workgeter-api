from django.contrib import admin
from django.urls import path, include
from tinder.views import CandidatosViewSet, EmpresaViewSet, VagaViewSet, FormularioViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('candidatos', CandidatosViewSet, basename='Candidatos')
router.register('empresas', EmpresaViewSet, basename='Empresas')
router.register('vagas',VagaViewSet, basename='Vagas')
router.register('formularios',FormularioViewSet, basename='Formularios')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
