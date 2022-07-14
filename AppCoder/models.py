from django.db import models


class Persona (models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)


class Contacto(Persona):

    domicilio = models.CharField(max_length= 50)
    altura = models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()

class Info_Adicional (Contacto,Persona):

    profesion = models.CharField( max_length=50)
    estado_civil = models.CharField(max_length=20)
    nacionalidad = models.CharField(max_length=50)