from django.db import models

class Libro(models.Model):
    nombre = models.CharField('Nombre', max_length = 100)
    autor  = models.CharField('Autor', max_length =200)
    genero = models.CharField('Genero', max_length =200)
 
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', max_length = 100)
    apellido = models.CharField('Apellido', max_length =200)

    def __str__(self):
        return '{0},{1}'.format(self.apellido,self.nombre)



