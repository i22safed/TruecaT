from django.shortcuts import render_to_response
from principal.models import Articulo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # Paginador
from django.template import RequestContext

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
