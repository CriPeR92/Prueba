from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Opcionale(models.Model):
    user = models.OneToOneField(User)
    
    telefono = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.user.username

    class Meta:
        permissions = (
            # Permission identifier     human-readable permission name
            ("Prueba1",               "pola"),
            ("Prueba2",                "klasd"),
            ("Prueba3",               "sd;lamsdklal"),
        )