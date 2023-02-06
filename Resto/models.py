from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    DNI = models.CharField(unique=True, max_length=10, null=True, blank=True)
    telefono = models.CharField(max_length=15)


class Sucursal(models.Model):
    ARG = 'Buenos Aires Argentina'
    PER = 'Lima Peru'
    COL = 'Bogota Colombia'
    BRA = 'Sao Paulo Brasil'

    Seleccion_Sucursal = (
        (ARG, 'Buenos Aires Argentina'),
        (PER, 'Lima Peru'),
        (COL, 'Bogota Colombia'),
        (BRA, 'Sao Paulo Brasil')
    )

    Ciudad = models.CharField(max_length=30,choices=Seleccion_Sucursal,default=ARG)



class Reservacion(models.Model):
    nombre= models.CharField(max_length=60)
    DNI= models.CharField(unique=True, max_length=10, null=True, blank=True)
    numero_mesa = models.IntegerField()
    num_invitados = models.IntegerField()
    fecha_de_reservacion = models.DateField()
