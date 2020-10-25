from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Libro


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =[
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'email' : 'Correo',
        }
        pass
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'
