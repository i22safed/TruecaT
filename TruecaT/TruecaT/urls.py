#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


admin.autodiscover()

urlpatterns = patterns('',

    # Admin

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc',include('django.contrib.admindocs.urls')),

    # Principal

    url(r'^$','principal.views.base'),

    # Urls de los modelos

    # Articulos

    url(r'^usuario/(?P<id_usuario>\d+)$','principal.views.id_usuario'),
    url(r'^articulos/$','principal.views.articulos'),
	url(r'^articulo/(?P<id_articulo>\d+)$','principal.views.id_articulo'),
	url(r'^articulo/nuevo/$','principal.views.nuevo_articulo'),

    url(r'^modificar/(?P<id_articulo>\d+)$', 'principal.views.modificar_articulo'),
	url(r'^eliminar/(?P<id_articulo>\d+)$', 'principal.views.eliminar_articulo'),
	url(r'^busqueda/$' ,'principal.views.busqueda'),
	url(r'^btitulo', 'principal.views.btit'),
	url(r'^bprovincia', 'principal.views.bprov'),
	url(r'^bcategoria', 'principal.views.buscat'),
	url(r'^comentario/(?P<id_articulo>\d+)$', 'principal.views.comentario'),

    url(r'^usuario/nuevo$','principal.views.nuevo_usuario'),
	url(r'^ingresar/$','principal.views.ingresar'),
	url(r'^privado/$','principal.views.privado'),
	url(r'^cerrar/$','principal.views.cerrar'),
	url(r'^editar/(?P<id_usuario>\d+)$', 'principal.views.editar'),

	url(r'^buzon/$', 'principal.views.buzon'),
	url(r'^buzon/enviar$','principal.views.enviarMensaje'),
	url(r'^buzon/leer/(?P<id_mensaje>\d+)$','principal.views.leermensaje'),
	url(r'^buzon/enviados$','principal.views.enviados'),

)x
