from django.contrib import admin
from usuario.models import Opcionale
from django.contrib.auth.models import Permission
from test.regrtest import dash_R
# Register your models here.

admin.site.register(Opcionale)
admin.site.register(Permission)