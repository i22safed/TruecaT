from django.shortcuts import render_to_response, render , get_object_or_404, redirect
from principal.models import Articulo, Provincia, Categoria, PerfilUsuario, Comentario, Mensaje

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Paginador
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from TruecaT.forms import SignUpForm,ArticuloForm,ComentarioForm,NuevoMensaje,modificarForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView, DetailView

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def base(request):
    return render_to_response('base.html',{'base':base}, context_instance = RequestContext(request))



def articulos(request):
    articulos = Articulo.objects.all()
    paginator = Paginator(articulos,4)
    page = request.GET.get('page')

    try:
        articulos = paginator.page(page)

    except PageNotAnInteger:
        articulos = paginator.page(1)

    except EmptyPage:
        articulos = paginator.page(paginator.num_pages)

    return render_to_response('articulos.html',{'articulos':articulos},
    context_instance = RequestContext(request))




def id_articulo(request, id_articulo):
    id_articulo = get_object_or_404(Articulo, pk = id_articulo)
    comentario = Comentario.objects.filter(articulo = id_articulo)
    return render_to_response ('articulo.html',{'articulo':id_articulo,'comentarios':comentarios},
    context_instance = RequestContext(request))




def nuevo_usuario(request):
    if request.method == 'POST':
        formulario = SignUpForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else: render_to_response('nuevo_usuario.html',{'formulario':formulario},
    context_instance = RequestContext(request))




def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate (username = usuario, password = clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request,acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render_to_response('noactivo.html',context_instance = RequestContext(request))

            else:
                return render_to_response('nousuario.html', context_instance = RequestContext(context))

        else:
            formulario = AuthenticationForm()
            return render_to_response('login.html',{'formulario':formulario}, context_instance = RequestContext(request))




@login_required(login_url = '/ingresar')
def privado (request):
    usuario = request.user
    return render_to_response('privado.html',{'usuario':usuario}, context_instance = RequestContext(request))




@login_required(login_url = '/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')




@login_required(login_url='/ingresar')
def nuevo_articulo(request):
    usuario = request.user
    if request.method == 'POST':
        formulario = ArticuloForm(request.POST, request.FILES)

        if formulario.is_valid():
                com = formulario.save(commit = False)
                com.usuario = request.user
                com.save()
                return HttpResponseRedirect('/articulos')
    else:

        data = {'usuario':request.user.username}
        formulario = ArticuloForm(initial = data)
    return render_to_response('nuevoarticulo.html',{'formulario':formulario,'usuario':usuario},
    context_instance = RequestContext(request))





@login_required(login_url = '/login')
def modificar_articulo(request, id_articulo):
    articulo = Articulo.objects.get(pk = id_articulo)
    if articulo.usuario.username == request.user.username:
        if request.method == 'POST':
            formulario = ArticuloForm(request.POST, request.FILES, instance = articulo)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect('/articulo/'+id_articulo)
        else:
            formulario = ArticuloForm(instance = artiuclo)
            context = {'formulario':formulario}
            return render(request, 'nuevoarticulo.html', context)
    else:
        return render_to_response ('sinpermiso.html',
        {'articulo':articulo},context_instance = RequestContext(request))




@login_required(login_url = '/login')
def eliminar_articulo (request, id_articulo):
    articulo = Articulo.objects.get(pk = id_articulo)
    if articulo.usuario.username == request.user.username:
        articulo = get_object_or_404(Articulo , pk = id_articulo)
        articulo.delete()
        return render(request, 'eliminado.html')
    else:
        return render(request,'sinpermiso.html')


def id_usuario(request, id_usuario):
    id_usuario = get_object_or_404(User, pk = id_usuario)
    usuart = Articulo.objects.filter(usuario = id_usuario)
    return render_to_response('usuario.html',{'usuario':id_usuario,'usuart':usuart},
    context_instance = RequestContext(request))


def busqueda(request):
    provincia = Provincia.objects.all()
    categoria = Categoria.objects.all()

    return render_to_response ('busqueda.html', {'provincia':provincia, 'categoria':categoria},
    context_instance = RequestContext(request))



def btit(request):
    titulo = request.GET['titulo']
    articulo = Articulo.objects.filter(titulo__contains = titulo)
    return render_to_response('btitulo.html',{'articulo':articulo},
    context_instance = RequestContext(request))


def bprov(request):
    provincia = request.GET['provincia']
    articulo = Articulo.objects.filter(Provincia__nombre__contains = provincia)
    return render_to_response('bprov.html',{'articulo':articulo},
    context_instance = RequestContext(request))


def buscat(request):
    categoria = request.GET['categoria']
    articulo = Articulo.objects.filter(Categoria__nombre__contains = categoria)
    return render_to_response('bcat.html',{'articulo':articulo},
    context_instance = RequestContext(request))


@login_required(login_url = '/login')
def comentario(request, id_articulo):
    what = Articulo.objects.get(pk = id_articulo)
    if request.method == 'POST':
        formucomentario = ComentarioForm(request.POST, request.FILES)
        if formucomentario.is_valid():
                comi = formucomentario.save(commit = False)
                comi.usuario = request.user
                comi.articulo = what
                comi.save()
                return HttpResponseRedirect('/articulo/'+id_articulo)
        else:
            formucomentario = ComentarioForm()
            return render_to_response ('comentarioform.html',{'formucomentario':formucomentario},
            context_instance = RequestContext(request))



@login_required(login_url = '/login')
def buzon(request):
    user = request.user
    list = Mensaje.objects.filter(to = user).order_by('leido').order_by('-date')
    context = {'recibidos' : list}
    return render(request, 'buzon.html',context)


@login_required(login_url = '/login')
def enviarMensaje(request):
    user = request.user
    if request.method == 'POST':
        form = nuevomensaje(request.POST)

        if form.is_valid():

            mensaje = form.save(commit = False)
            mensaje.fromu = get_object_or_404(User, pk = user.id)
            mensaje.save()
            return redirect('/buzon')

        else:

            form = nuevomensaje()
            context = {'form':form}
            return render(request, 'enviar.html', context)



@login_required(login_url = '/login')
def leermensaje(request, id_mensaje):
    mensaje = Mensaje.objects.get(pk = id_mensaje)
    mensaje.leido = False
    mensaje.save()
    context = {'mensaje':mensaje}
    return render(request, 'mensaje.html', context)


@login_required(login_url = '/login')
def enviados(request):
    user = request.user
    list = Mensaje.objects.filter(fromu = user).order_by('-date')
    context = {'enviados': list}
    return render(request, 'enviados.html', context)


@login_required(login_url = '/login')
def editar(request, id_usuario):

    user = get_object_or_404(PerfilUsuario, pk = id_usuario)
    if request.method == 'POST':
        form = modificarForm(request.POST, instance = user)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/privado')

    else:
        form = modificarForm(instance = user)
        return render(request, 'editar.html', {'form':form})
