from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class PerfilUsuario(User):
    provincia = models.CharField(max_length = 50, null = True)
    ciudad = models.CharField(max_length = 50, null = True)
    tlf = models.IntegerField(null = True)

class Provincia(models.Model):
    nombre = models.CharField(max_length = 50, unique = True)

    def __unicode__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50, unique = True)
    def __unicode__(self):
        return self.nombre


class Articulo(models.Model):

    nombre = models.CharField(max_length=100)
    Categoria = models.ForeignKey(Categoria)
    imagen = models.ImageField(upload_to = 'img',verbose_name = 'Imagen', null = True, blank = True)
    descripcion = models.TextField()
    oferta = models.TextField()
    usuario = models.ForeignKey(User)
    Provincia = models.ForeignKey(Provincia)
    fecha = models.DateTimeField(default=datetime.datetime.now)
    numero = models.IntegerField()

    def __unicode__(self):
        return self.nombre
