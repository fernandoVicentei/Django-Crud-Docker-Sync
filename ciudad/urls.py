from django.urls import path
from . import views

app_name = 'ciudad'

urlpatterns = [
    path('', views.listar_ciudades, name='listar'),
    path('crear/', views.crear_ciudad, name='crear'),
    path('editar/<int:id>/', views.editar_ciudad, name='editar'),
    path('eliminar/<int:id>/', views.eliminar_ciudad, name='eliminar'),
    #path('restaurar/<int:id>/', views.restaurar_ciudad, name='restaurar'),
    path('por-pais/<int:pais_id>/', views.ciudades_por_pais, name='por_pais'),
]