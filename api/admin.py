from django.contrib import admin
from .models import Persona,Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ['nombre','autor','genero']

admin.site.register(Persona)
admin.site.register(Libro)

