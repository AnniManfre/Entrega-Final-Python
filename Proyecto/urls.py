from django.urls import path
from . import views



urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('sobre_nosotros/', views.sobre_nosotros, name='Sobre Nosotros'),
    path('ver_datos_almacenados/', views.ver_datos_almacenados, name='Ver Datos'),
    path('ingresar_datos/', views.ingresar_datos, name='Ingresar Datos'),
    path('eliminar_dato/<int:pk>/', views.DatosAlmacenadosDelete.as_view(), name='Eliminar'),

]
