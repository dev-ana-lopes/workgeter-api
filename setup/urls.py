from django.contrib import admin
from django.urls import path, include
from tinder.views import CandidatosViewSet, EmpresaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('candidatos', CandidatosViewSet, basename='Candidatos')
router.register('empresas', EmpresaViewSet, basename='Empresas')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
