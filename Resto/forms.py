from django import forms 


class registrar(forms.Form):
    nombre = forms.CharField(max_length=60)
    DNI = forms.CharField()
    telefono = forms.IntegerField()


ARG = 'Buenos Aires Argentina'
PER = 'Lima Peru'
COL = 'Bogota Colombia'
BRA = 'Sao Paulo Brasil'

sucursales = [
        (ARG, 'Buenos Aires Argentina'),
        (PER, 'Lima Peru'),
        (COL, 'Bogota Colombia'),
        (BRA, 'Sao Paulo Brasil')
    ]
class escoger_Sucursal(forms.Form):

    Ciudad = forms.ChoiceField(choices=sucursales,widget=forms.Select, initial=ARG)
    

class genera_reserva(forms.Form):
    nombre= forms.CharField(max_length=60)
    DNI= forms.CharField(max_length=10)
    numero_mesa = forms.IntegerField()
    num_invitados = forms.IntegerField()
    fecha_de_reservacion = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))



