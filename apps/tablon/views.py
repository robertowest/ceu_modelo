from bdb import set_trace
from django.http import HttpResponse
from django.shortcuts import render

from dbschema.models import Area, TipoTitulacion, Campus, TitulacionesView
from . import utilities


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    template = 'tablon/index.html'
    
    if request.method == 'POST':
        context = {
            'tipostitulaciones': utilities.obtenerTipoTitulaciones(),
            'titulaciones': utilities.obtenerTitulaciones(),
            'asignaturas': utilities.obtenerAsignaturas(request.POST.get('titulaciones', '')),
        }
    else:
        context = {
            'tipostitulaciones': utilities.obtenerTipoTitulaciones(),
            'titulaciones': utilities.obtenerTitulaciones(),
            'asignaturas': [],
        }
    return render(request, template, context)



def tablon(request):
    return render(request, 'tablon/tablon.html', context={'asignaturas': utilities.obtenerAsignaturas('2011')})




from django.http import JsonResponse
from django.db.models import Q
from django.template import RequestContext


def getContext():
    return {
        'tipos': TipoTitulacion.objects.filter(deleted=False).order_by('nombre'),
        'campus': Campus.objects.filter(deleted=False).order_by('nombre'),
        'areas': Area.objects.filter(deleted=False, parent_id__isnull=True).order_by('nombre'),
        'titulaciones': {},
    }

    
def base(request):
    return render(request, 'tablon/base.html', context=getContext())


def tablon_buscar_ajax(request):
    if request.is_ajax():
        filtro = Q()
        if request.GET.get('tipo', '') != '':
            filtro = filtro & Q(tipo_id = request.GET['tipo'])
            
        if request.GET.get('campus', '') != '':
            filtro = filtro & Q(campus_id = request.GET['campus'])
            
        if request.GET.get('area', '') != '':
            filtro = filtro & Q(area_id = request.GET['area'])

        # return JsonResponse( { 'mensaje': str(filtro) } )
        content = getContext()
        content['titulaciones'] = TitulacionesView.objects.filter(filtro)
        return render(request, 'tablon/base.html', content)        

    return base(request)


# https://secure.infomed.es:443/AgendaOnline/SOAS.dll/infmd/rest/TRemoteAgent/DameAgendas/PZ5GTAHJ-7GXZ2EXM-EZ3P6HJU-RO12DEZH/
