from django.contrib import admin
from principal.models import PerfilUsuario, Categoria, Provincia, Articulo, Comentario, Mensaje

# Register your models here.

admin.site.register(PerfilUsuario)
admin.site.register(Categoria)
admin.site.register(Articulo)
admin.site.register(Provincia)
admin.site.register(Comentario)
admin.site.register(Mensaje)
