from django.urls import path
from . import views
from Resto.views import *

urlpatterns = [
    path('', views.inicio, name='Inicio'),
    path('sucursal/', Pais, name = 'Sucursal' ), 
    path('registro/', Registro, name = 'Registro' ),
    path('reserva/', Reserva, name = 'Reserva'),
    path('registrar_cliente/', registrar_cliente, name = 'Registros'),
    path('nueva_sucursal/', choice_sucursal, name = 'Nueva sucursal'),
    path('nueva_reserva/', creacion_reserva, name= 'Nueva Reserva'),
    path('buscar_reserva/', busqueda_reserva, name= 'BuscarReserva'),
    path('resultados/', resultados_reservas, name= 'Resultados'),

    
    
]
