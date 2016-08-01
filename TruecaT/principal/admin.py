from django.contrib import admin
from principal.models import PerfilUsuario, Categoria, Provincia, Articulo

# Register your models here.

admin.site.register(PerfilUsuario)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Provincia)
