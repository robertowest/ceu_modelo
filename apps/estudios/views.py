from bdb import set_trace
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from dbschema.models import Area, AreaTitulacion, Campus, TipoTitulacion, Titulacion, TitulacionesView

from . import utilities


def amador(request):
    """Carga datos desde url json"""
    template = 'estudios/amador.html'
    
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


def ejemplo_estudios(request):
    """Ejemplo completo del tablón html"""
    return render(request, 'estudios/ejemplo_estudios.html', context={'asignaturas': utilities.obtenerAsignaturas('2011')})


# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------


def index(request):
    contenido = {
        'tipos': TipoTitulacion.objects.values('id', 'nombre').filter(deleted=False).order_by('nombre'),
        'campus': Campus.objects.values('id', 'nombre').filter(deleted=False).order_by('nombre'),
        'areas': Area.objects.values('id', 'nombre', 'icono').filter(deleted=False, parent_id__isnull=True).order_by('nombre')
    }
    return render(request, 'estudios/index.html', context=contenido)


def estudios_buscar_ajax_CON_TEMPLATE(request):
    # if request.is_ajax():
    #     # # obtenemos todas las subareas de un area
    #     # s = Area.objects.filter(parent_id=9).values_list('id', flat=True)
    #     # # obtenemos todas las titulaciones relacionadas a las subareas
    #     # ar = AreaTitulacion.objects.filter(area__in=s).values_list('titulacion', flat=True)
    #     # # obtenemos las titulaciones
    #     # t = Titulacion.objects.filter(id__in=ar)

    #     # Titulacion.objects.get(id=1).area.all()
    #     # Titulacion.area.through.objects.all()
        
    #     filtro = Q()
    #     if request.GET.get('tipo', '') != '':
    #         filtro = filtro & Q(tipo_titulacion_id = request.GET['tipo'])
            
    #     if request.GET.get('campus', '') != '':
    #         filtro = filtro & Q(campus_id = request.GET['campus'])
            
    #     if request.GET.get('area', '') != '':
    #         # areas_id = Area.objects.filter(parent_id=request.GET['area']).values_list('id', flat=True)
    #         # filtro = filtro & Q(area_id__in=areas_id)
    #         filtro = filtro & Q(area_id = request.GET['area'])

    #     context = { 'titulaciones': TitulacionesView.objects.filter(filtro) }
    #     return render(request, 'estudios/includes/titulaciones.html', context)

    # return index(request)
    pass

def estudios_buscar_ajax(request):
    if request.is_ajax():
        filtro = Q()
        if request.GET.get('tipo', '') != '':
            filtro = filtro & Q(tipo_titulacion_id = request.GET['tipo'])
            
        if request.GET.get('campus', '') != '':
            filtro = filtro & Q(campus_id = request.GET['campus'])
            
        if request.GET.get('area', '') != '':
            filtro = filtro & Q(area_id = request.GET['area'])

        titulaciones = TitulacionesView.objects.filter(filtro)
        html = ''
        
        if titulaciones:
            # si existen titulaciones, creamos la estructura de acordeon
            encabezado = '<div class="acordeon"><h3 class="tag">{0}</h3><div class="acordeon-box" style=""><ul class="list-info list-info-none">' + \
                         '<li><span class="description">&nbsp;</span><strong class="lang">Idioma</strong><strong class="years">Duración</strong>' + \
                         '<strong class="etcs">Créditos</strong></li></ul><ul class="list-info">'
            iteracion = '<li><span class="description">{0}</span><span class="lang">{1}</span><span class="years">{2} {3}</span><span class="etcs">{4} ETCS</span></li>'
            cierre = '</ul><br></div></div>'
            
            control_cut = 0
            for obj in titulaciones:
                if control_cut != obj.subarea_id:
                    if control_cut != 0:
                        html += cierre
                    html += encabezado.format(obj.subarea)
                    control_cut = obj.subarea_id
                html += iteracion.format(obj.titulacion, 'esp', obj.duracion, obj.get_duracion_tipo_display(), obj.creditos)
            html += cierre
            
        return HttpResponse('<div class="cover-acordeon">' + html + '</div>')
    
    return index(request)


# cita previa odontologia
# https://secure.infomed.es:443/AgendaOnline/SOAS.dll/infmd/rest/TRemoteAgent/DameAgendas/PZ5GTAHJ-7GXZ2EXM-EZ3P6HJU-RO12DEZH/


# sa=Area.objects.filter(parent_id=2).values_list('id', flat=True)  # comunicaciones
# relacion = AreaTitulacion.objects.filter(area__in=sa)
