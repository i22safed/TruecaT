#encoding: utf-8

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    # Admin

    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc',include('django.contrib.admindocs.urls')),

    # Principal

    url(r'^$','principal.views.base'),

    # Urls de los modelos

    # Articulos

    url(r'^articulos/$','principal.views.articulos'),


)
