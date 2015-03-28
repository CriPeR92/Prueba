from django.db import models
from django.contrib.auth.models import User

"""Datos opcionales del usuario.
Aqui se agregan los campos opcionales del usuario 
"""
class Usuario(User):
    direccion = models.CharField(max_length=250, blank=True)
    telefono = models.PositiveIntegerField(null=True, blank=True)
