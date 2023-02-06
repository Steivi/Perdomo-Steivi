from django.shortcuts import render
from django.http import HttpResponse
from Resto.models import *
from Resto.forms import *

# Create your views here.

def inicio(request):
    return render(request, "Resto/inicio.html")

def Pais(request):
   return render(request,"Resto/sucursal.html")

def Registro(request):
    return render(request, "Resto/registro.html")

def Reserva(request):
    return render(request, "Resto/reservacion.html")

def registrar_cliente(request):
    if request.method == "POST":

        formulario1 = registrar(request.POST)
        
        if formulario1.is_valid():

            info = formulario1.cleaned_data

            rnuevo= Cliente(nombre = info["nombre"], DNI= info["DNI"], telefono= info["telefono"])

            rnuevo.save()

            return render(request,"Resto/inicio.html")
        
    else:
        formulario1 = registrar()
    
    return render(request, "Resto/registro.html", {"form1" : formulario1})

def choice_sucursal(request):
    if request.method == "POST":

        formulario2= escoger_Sucursal(request.POST)
        if formulario2.is_valid():

            info = formulario2.cleaned_data

            nciudad= Sucursal(Ciudad= info["Ciudad"])

            nciudad.save()
        
            return render(request,"Resto/inicio.html")
        
    else:
        formulario2 = escoger_Sucursal()

    return render(request, "Resto/sucursal.html", {"form2" : formulario2})

def creacion_reserva(request):
    if request.method == "POST":

        formulario3= genera_reserva(request.POST)
        if formulario3.is_valid():

            info = formulario3.cleaned_data

            nreserva= Reservacion(nombre= info["nombre"], DNI= info["DNI"], numero_mesa= info["numero_mesa"], num_invitados= info["num_invitados"], fecha_de_reservacion= info["fecha_de_reservacion"])

            nreserva.save()
        
            return render(request,"Resto/inicio.html")
        
    else:
        formulario3 = genera_reserva()

    return render(request, "Resto/reservacion.html", {"form3" : formulario3})



def busqueda_reserva(request):

    return render(request, "Resto/inicio.html")

def resultados_reservas(request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]
        reserva= Reservacion.objects.filter(nombre__icontains = nombre)

        return render(request, "Resto/inicio.html" , {"reserva":reserva, "nombre": nombre})
    
    else:

        respuesta= "No Enviastes Datos"

    return HttpResponse(respuesta)


    