from django import forms
from .models import Usuarios

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios 
        fields = '__all__'

        labels = {
            'cedula': 'Cédula',
            'nombre' : 'Primer nombre',
            'apellido' : 'Primer apellido' ,
            'correo' : 'Correo'
        }

        widgets  ={
            'cedula' : forms.NumberInput(attrs={'placeholder': 'eg. 1234567890'}),
            'nombre' : forms.TextInput(attrs={'placeholder': 'eg. Juan'}),
            'apellido' : forms.TextInput(attrs={'placeholder': 'eg. Barbosa'}),
            'correo' : forms.EmailInput(attrs={'placeholder': 'eg. abc@xyz.com'}),
        }