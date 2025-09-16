from django.urls import path
from . import views

app_name = 'pais'

urlpatterns = [
    path('', views.listar_paises, name='listar'),
    path('crear/', views.crear_pais, name='crear'),
    path('editar/<int:id>/', views.editar_pais, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_pais, name='eliminar'),
    path('listado-integrado/', views.listado_integrado, name='listado_integrado'),
]