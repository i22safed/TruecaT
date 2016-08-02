
#encoding: utf-8

from django.forms import ModelForm
from django import forms
from principal.models import PerfilUsuario, Articulo, Comentario, Mensaje

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Aqui crearemos cada uno de los formularios pertinentes

class SignUpForm(UserCreationForm):
    class Meta:
        model =  PerfilUsuario
        fields = ['first_name','last_name','email','provincia','ciudad','username']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['email'].label = "Email"
        self.fields['provincia'].label = "Provincia"
        self.fields['ciudad'].label = "Ciudad"
        self.fields['username'].label = "Nombre de usuario"

class ArticuloForm(ModelForm):
    class Meta:
        model = Articulo
        exclude = ['usuario','fecha']


class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario
        exclude = ['usuario','fecha','articulo']

class NuevoMensaje(ModelForm):
    class Meta:
        model = Mensaje

class modificarForm(ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['first_name','last_name','email','provincia','ciudad']


    def __init__(self, *args, **kwargs):
        super(modificarForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Nombre"
        self.fields['last_name'].label = "Apellidos"
        self.fields['email'].label = "Email"
        self.fields['provincia'].label = "Provincia"
        self.fields['ciudad'].label = "Ciudad"
