from django.contrib import admin
from usuario.models import Opcionale
from django.contrib.auth.models import Permission
# Register your models here.

admin.site.register(Opcionale)
admin.site.register(Permission)