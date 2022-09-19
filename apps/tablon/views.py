import json
import requests

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def index(request):
    # grados y posgrados
    # http://desa01.ceu.es/Webservices/Uch/WebApiPlanesEstudiosWeb/api/PlanesEstudios?soloGradosPostgrados=true&soloPlanesConHitos=false
    
    # asignaturas
    # {0} = IdPlanEstudioNK
    # http://desa01.ceu.es/Webservices/Uch/WebApiPlanesEstudiosWeb/api/PlanesEstudios/v2/{0}?incluirPeriodos=false&incluirIdiomas=false&incluirHitos=false
    
    template = 'tablon/index.html'
    context = {}
    return render(request, template, context)


def obtenerTitulaciones():
    resp = requests.get('http://desa01.ceu.es/Webservices/Uch/WebApiPlanesEstudiosWeb/api/PlanesEstudios?soloGradosPostgrados=true&soloPlanesConHitos=false')


def obtenerAsignaturas(plan_id):
    resp = requests.get('http://desa01.ceu.es/Webservices/Uch/WebApiPlanesEstudiosWeb/api/PlanesEstudios/v2/{0}?incluirPeriodos=false&incluirIdiomas=false&incluirHitos=false'.format(plan_id))
   
