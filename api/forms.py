from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Libro


class CustomUserForm(UserCreationForm):
    pass

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'