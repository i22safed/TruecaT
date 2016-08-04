# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coment', models.TextField(help_text=b'Escriba aqui su comentario', null=True, verbose_name=b'Comentario', blank=True)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('articulo', models.ForeignKey(to='principal.Articulo')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('texto', models.TextField()),
                ('leido', models.BooleanField(default=True)),
                ('fromu', models.ForeignKey(related_name='fromu', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('to', models.ForeignKey(related_name='to', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='articulo',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
