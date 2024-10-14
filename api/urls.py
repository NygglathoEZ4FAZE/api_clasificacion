from django.urls import path
from .views import ClasificarConsulta

urlpatterns = [
    path('clasificar/', ClasificarConsulta.as_view(), name='clasificar_consulta'),
]
