#!/usr/bin/python3

# ---------------------------------------------------------
# configuración necesaria para utilizar el ORM de Django
# ---------------------------------------------------------

# configuración específica de Django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# asegúrese de que se lean la configuración
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


# -----------------------------------------------------------------------------------
# recupera los datos de las API's de Amador y las graba en el modelo propio de la web
# -----------------------------------------------------------------------------------



# PENSAR COMO MODIFICAR LOS DATOS 
# CUANDO SE MODIFIQUE EL CURSO AL QUE PERTENECE UNA ASIGNATURA
# (posiblemente tengamos que borrar cursos_asignaturas y volver a crear la referencia)





import json
import requests

from dbschema.models import Asignatura, AsignaturaIdioma, Campus, Curso, CursoAsignatura, PlanEstudio, TipoTitulacion, Titulacion, TitulacionIdioma


# obtenemos los datos de campus
def obtenerCampus():
    # resp = requests.get('http://desa01.ceu.es/Webservices/Uch/WebApiPlanesEstudiosWeb/api/Campus')
    # if resp.status_code == 200:
    #     campus = resp.json()
    return [
        {
            "IdCampusNK": 1,
            "NombreCampus": "Valencia"
        },
        {
            "IdCampusNK": 2,
            "NombreCampus": "Elche"
        },
        {
            "IdCampusNK": 3,
            "NombreCampus": "Castellón"
        }
    ]


def obtenerTitulaciones():
    return [
        {
            "IdPlanEstudioNK": 130,
            "NombrePlanEstudio": "Architecture (Grado en Fundamentos de Arquitectura)",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 135,
            "NombrePlanEstudio": "Doble Grado Derecho y Ciencias Políticas y de la Administración",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 150,
            "NombrePlanEstudio": "Doble Grado Educación Infantil y Educación Primaria",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 151,
            "NombrePlanEstudio": "Doble Grado Educación Primaria y Educación Infantil",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 182,
            "NombrePlanEstudio": "Doble Grado en Ciencias de la Actividad Física y el Deporte + Educación Primaria",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 140,
            "NombrePlanEstudio": "Doble Grado en Ciencias Políticas / Relaciones Internacionales + Periodismo",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 141,
            "NombrePlanEstudio": "Doble Grado en Ciencias Políticas y de la Administración y Dirección de Empresas",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 139,
            "NombrePlanEstudio": "Doble Grado en Ciencias Políticas/Relaciones Internacionales + Publicidad y Relaciones Públicas",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 148,
            "NombrePlanEstudio": "Doble Grado en Comunicación Audiovisual + Periodismo",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 149,
            "NombrePlanEstudio": "Doble Grado en Comunicación Audiovisual + Publicidad y Relaciones Públicas",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 137,
            "NombrePlanEstudio": "Doble Grado en Derecho + Publicidad y Relaciones Públicas",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 136,
            "NombrePlanEstudio": "Doble Grado en Derecho y Dirección de Empresas",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 174,
            "NombrePlanEstudio": "Doble Grado en Dirección de Empresas y Derecho",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 138,
            "NombrePlanEstudio": "Doble Grado en Dirección de Empresas y Marketing",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 179,
            "NombrePlanEstudio": "Doble Grado en Dirección de Empresas y Título de Especialista en Dirección y Gestión Deportiva",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 176,
            "NombrePlanEstudio": "Doble Grado en Farmacia y Nutrición Humana y Dietética",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 175,
            "NombrePlanEstudio": "Doble Grado en Marketing y Publicidad y RR.PP.",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 142,
            "NombrePlanEstudio": "Doble Grado en Periodismo + Ciencias Políticas / Relaciones Internacionales",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 147,
            "NombrePlanEstudio": "Doble Grado en Periodismo + Comunicación Audiovisual",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 146,
            "NombrePlanEstudio": "Doble Grado en Periodismo + Publicidad y Relaciones Públicas",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 145,
            "NombrePlanEstudio": "Doble Grado en Publicidad y Relaciones Públicas + Comunicación Audiovisual",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 143,
            "NombrePlanEstudio": "Doble Grado en Publicidad y Relaciones Públicas + Marketing",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 144,
            "NombrePlanEstudio": "Doble Grado en Publicidad y Relaciones Públicas + Periodismo",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 152,
            "NombrePlanEstudio": "Doble Grado Fisioterapia y Enfermería",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 123,
            "NombrePlanEstudio": "Grado en Arquitectura (Architecture)",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 181,
            "NombrePlanEstudio": "Grado en Ciencias de la Actividad Física y el Deporte",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 126,
            "NombrePlanEstudio": "GRADO EN CIENCIAS POLÍTICAS",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 165,
            "NombrePlanEstudio": "Grado en Ciencias Políticas + Título de Experto en Marketing y Comunicación Política",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 110,
            "NombrePlanEstudio": "Grado en Comunicación Audiovisual",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 157,
            "NombrePlanEstudio": "Grado en Comunicación Audiovisual + Título de Especialista en Comunicación de Moda",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 121,
            "NombrePlanEstudio": "Grado en Derecho",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 156,
            "NombrePlanEstudio": "Grado en Derecho + Título de Especialista en Derecho Internacional y Derecho Europeo",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 166,
            "NombrePlanEstudio": "Grado en Derecho + Título de Especialista en Integración Europea y Mercado Exterior",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 119,
            "NombrePlanEstudio": "GRADO EN DIRECCIÓN DE EMPRESAS",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 161,
            "NombrePlanEstudio": "Grado en Dirección de Empresas + Título de Especialista en Integración Europea y Mercado Exterior",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 127,
            "NombrePlanEstudio": "Grado en Educación Infantil",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 1
        },
        {
            "IdPlanEstudioNK": 128,
            "NombrePlanEstudio": "Grado en Educación Primaria",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 12
        },
        {
            "IdPlanEstudioNK": 111,
            "NombrePlanEstudio": "GRADO EN ENFERMERÍA",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 112,
            "NombrePlanEstudio": "GRADO EN FARMACIA",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 153,
            "NombrePlanEstudio": "Grado en Farmacia + Título Experto Gestión y Marketing de la oficina de Farmacia",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 113,
            "NombrePlanEstudio": "GRADO EN FISIOTERAPIA",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 120,
            "NombrePlanEstudio": "GRADO EN INGENIERÍA EN DISEÑO INDUSTRIAL Y DESARROLLO DE PRODUCTOS",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 129,
            "NombrePlanEstudio": "Grado en Marketing",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 162,
            "NombrePlanEstudio": "Grado en Marketing + Título de Especialista en Integración Europea y Mercado Exterior",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 124,
            "NombrePlanEstudio": "Grado en Medicina",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 164,
            "NombrePlanEstudio": "Grado en Medicina + Título de Experto en Medicina Integrada",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 134,
            "NombrePlanEstudio": "Grado en Nutrición Humana y Dietética (Plan/2016)",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 125,
            "NombrePlanEstudio": "GRADO EN ODONTOLOGÍA",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 131,
            "NombrePlanEstudio": "Grado en Óptica y Optometría",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 117,
            "NombrePlanEstudio": "Grado en Periodismo",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 160,
            "NombrePlanEstudio": "Grado en Periodismo + Título de Especialista en Comunicación de Moda",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 154,
            "NombrePlanEstudio": "Grado en Periodismo + Título de Experto en Periodismo Deportivo",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 159,
            "NombrePlanEstudio": "Grado en Periodismo + Título Experto en Marketing y Comunicación Política",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 155,
            "NombrePlanEstudio": "Grado en Publicidad + Título Experto en Marketing y Comunicación Política",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 118,
            "NombrePlanEstudio": "Grado en Publicidad y Relaciones Públicas",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 163,
            "NombrePlanEstudio": "Grado en Publicidad y RRPP + Título de Especialista en Comunicación de Moda",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 122,
            "NombrePlanEstudio": "GRADO EN VETERINARIA",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 132,
            "NombrePlanEstudio": "Graduado/a en Gastronomía/Gastronomy",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 1,
            "NombrePlanEstudio": "Plan de Estudios de Movilidad",
            "IdTipoEstudioNK": 5,
            "NombreTipoEstudio": "Grado",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2014,
            "NombrePlanEstudio": "M.U. en Gestión de Instalaciones Energéticas e Internacionalización de Proyectos",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2003,
            "NombrePlanEstudio": "Máster UNIVERSITARIO DE ESPECIALIZACIÓN EN CUIDADOS DE ENFERMERÍA",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2011,
            "NombrePlanEstudio": "Máster Universitario en Abogacía",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2020,
            "NombrePlanEstudio": "Máster Universitario en Abogacía + Máster Propio en Derecho Internacional de los Negocios",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2022,
            "NombrePlanEstudio": "Máster Universitario en Arquitectura",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2004,
            "NombrePlanEstudio": "Máster Universitario en Comunicación Y Branding Digital",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2009,
            "NombrePlanEstudio": "Máster Universitario en Diseño de Interiores",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2017,
            "NombrePlanEstudio": "Máster Universitario en Diseño de Producto",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2016,
            "NombrePlanEstudio": "Máster Universitario en Diseño y Comunicación Gráfica",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2013,
            "NombrePlanEstudio": "Máster Universitario en Educación Bilingüe (Inglés y Español)",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 2
        },
        {
            "IdPlanEstudioNK": 2018,
            "NombrePlanEstudio": "Máster Universitario en Fisioterapia Deportiva",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2001,
            "NombrePlanEstudio": "Máster Universitario en Formación del Profesorado de Educación Secundaria Obligatoria y Bachillerato, Formación Profesional y Enseñanzas de Idiomas",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 11
        },
        {
            "IdPlanEstudioNK": 2012,
            "NombrePlanEstudio": "Máster Universitario en Gestión Ambiental",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 2
        },
        {
            "IdPlanEstudioNK": 2010,
            "NombrePlanEstudio": "Máster Universitario en Gestión de Proyectos e Instalaciones Energéticas",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2007,
            "NombrePlanEstudio": "Máster Universitario en Gestión y Dirección de Centros Educativos",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2006,
            "NombrePlanEstudio": "Máster Universitario en Ortodoncia y Ortopedia Dentofacial",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2019,
            "NombrePlanEstudio": "Máster Universitario en Psicología General Sanitaria",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2021,
            "NombrePlanEstudio": "Máster Universitario en Psicología Jurídica y Práctica Forense",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2008,
            "NombrePlanEstudio": "Máster Universitario en Seguridad Alimentaria",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 2015,
            "NombrePlanEstudio": "Máster Universitario en Técnicas Avanzadas Estéticas y Láser",
            "IdTipoEstudioNK": 6,
            "NombreTipoEstudio": "Máster Universitario",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3012,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Animales Exóticos",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3006,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Cirugía de Tejidos Blandos en Pequeños Animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3071,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Cirugía en Pequeños Animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3013,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Dermatología de Pequeños animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3005,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Diagnóstico por Imagen en Pequeños Animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3010,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Medicina felina",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3008,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Medicina Interna de Pequeños Animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4008,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Medicina Interna y Urgencias en Pequeños Animales.",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3011,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Neurología en Pequeños Animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3009,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Oftalmología de Pequeños Animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3007,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Traumatología en Pequeños Animales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4007,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Traumatología y Ortopedia. Sistemas de Fijación externa en Pequeños Animales.",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3002,
            "NombrePlanEstudio": "Curso Superior En Audiología Protésica",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3021,
            "NombrePlanEstudio": "Curso Superior en Gestión de Riesgos y Seguros",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3065,
            "NombrePlanEstudio": "Curso Universitario en Mediación Civil y Mercantil",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4171,
            "NombrePlanEstudio": "Diploma Universitario de Especialización en Comunicación de Moda",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4180,
            "NombrePlanEstudio": "Diploma Universitario de Especialización en Derecho Internacional y Derecho Europeo",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4060,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Cirugía Menor Ambulatoria",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3066,
            "NombrePlanEstudio": "Diploma Universitario de experto en Derecho del Arte",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4178,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Dirección y Gestión Deportiva",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4022,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Diseño de Producto para el Hábitat",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4023,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Diseño Gráfico y Comunicación",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4001,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Ecografía Músculo-esquelética",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4018,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Enseñanza Escolar de la Religión Católica",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4168,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Gestión de Oficina de Farmacia y Marketing Farmacéutico",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4004,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Helicopter Emergency Medical Service y Asistencia Médica Aerotransportada",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4065,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Mediación Civil y Mercantil",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4029,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Mediación y Resolución de Conflictos",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4025,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Neuromodulación Percutánea y Técnicas Invasivas",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4173,
            "NombrePlanEstudio": "DIPLOMA UNIVERSITARIO DE EXPERTO EN PERIODISMO DEPORTIVO",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4026,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Reeducación del Suelo Pélvico. Aplicación Ginecológica, Urológica, Obstétrica y Coloproctológica",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4064,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Showrunner en Ficción Audiovisual: Guión, Dirección y Producción de Series",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4172,
            "NombrePlanEstudio": "DIPLOMA UNIVERSITARIO DE FORMACIÓN AVANZADA EN FISIOTERAPIA ONCOLÓGICA",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3063,
            "NombrePlanEstudio": "European Master in Consumer Relationship Management",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3061,
            "NombrePlanEstudio": "M.P. en Cirugía Bucal e Implantología Bucofacial",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4182,
            "NombrePlanEstudio": "Máster de Formación Permanente en Cirugía Bucal ",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4063,
            "NombrePlanEstudio": "Máster de Formación Permanente en Customer Relationship Marketing",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4052,
            "NombrePlanEstudio": "Máster de Formación Permanente en Derecho Internacional de los Negocios",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4050,
            "NombrePlanEstudio": "Máster de Formación Permanente en Dirección Bursátil y Financiera",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4003,
            "NombrePlanEstudio": "Máster de Formación Permanente en Dirección y Monitorización de Ensayos Clínicos",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4051,
            "NombrePlanEstudio": "Máster de Formación Permanente en Especialización en Odontología Multidisciplinar Avanzada",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4016,
            "NombrePlanEstudio": "Máster de Formación Permanente en Especialización en Ortodoncia",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4053,
            "NombrePlanEstudio": "Máster de Formación Permanente en Especialización en Prótesis Avanzada",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4014,
            "NombrePlanEstudio": "Máster de Formación Permanente en Odontopediatría Integral",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4184,
            "NombrePlanEstudio": "Máster en Formación Permanente en Endodoncia/Master's Degree in Endodontics",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4017,
            "NombrePlanEstudio": "Máster en Formación Permanente en Odontología Conservadora y Endodoncia",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3057,
            "NombrePlanEstudio": "Master Program in Reasoning and Clinical practice for Physiotherapy",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3050,
            "NombrePlanEstudio": "Máster Propio Bursátil y Financiero",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3058,
            "NombrePlanEstudio": "MÁSTER PROPIO EN COMERCIO INTERNACIONAL Y NEGOCIO DIGITAL",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3054,
            "NombrePlanEstudio": "Máster Propio en Comunicación y Marketing Digital",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3052,
            "NombrePlanEstudio": "MÁSTER PROPIO EN DERECHO INTERNACIONAL DE LOS NEGOCIOS",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3003,
            "NombrePlanEstudio": "Máster Propio en Dirección y Monitorización de Ensayos Clínicos",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3051,
            "NombrePlanEstudio": "MÁSTER PROPIO EN ESPECIALIZACIÓN EN ODONTOLOGÍA MULTIDISCIPLINAR AVANZADA",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3016,
            "NombrePlanEstudio": "Máster Propio en Especialización en Ortodoncia",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3053,
            "NombrePlanEstudio": "Máster Propio en Especialización en Prótesis Avanzada",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3015,
            "NombrePlanEstudio": "Máster Propio en Implantología Oral",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3048,
            "NombrePlanEstudio": "Máster Propio en Neurociencias: cuidados médico-quirúrgicos y rehabilitación del paciente neurológico",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3017,
            "NombrePlanEstudio": "Máster Propio en Odontología Conservadora y Endodoncia",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3014,
            "NombrePlanEstudio": "Máster Propio en Odontopediatría",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3067,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Claves para el Diseño y la Arquitectura.",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4110,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Derecho Europeo",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4109,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Derecho Internacional",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4112,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Dirección Deportiva",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4021,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Gestión de Riesgos y Seguros",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4111,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Gestión Deportiva",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4024,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Interiorismo de Espacios Comerciales y Residenciales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3062,
            "NombrePlanEstudio": "Programa Empleabilidad Integral del Maestro",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 171,
            "NombrePlanEstudio": "Título de Especialista en Comunicación de Moda",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 180,
            "NombrePlanEstudio": "Título de Especialista en Derecho Internacional y Derecho Europeo",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 178,
            "NombrePlanEstudio": "Título de Especialista en Dirección y Gestión Deportiva",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 167,
            "NombrePlanEstudio": "Título de Especialista en Integración Europea y Mercado Exterior",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3022,
            "NombrePlanEstudio": "Titulo de Experto en Diseño de Producto para el Hábitat",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3023,
            "NombrePlanEstudio": "Título de Experto en Diseño Gráfico y Comunicación",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3001,
            "NombrePlanEstudio": "Título de Experto en Ecografía Músculo-esquelética",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3018,
            "NombrePlanEstudio": "Título de Experto en Enseñanza Escolar de la Religión Católica",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3028,
            "NombrePlanEstudio": "Título de Experto en Estatuto Jurídico del Menor. Coordinador de Parentalidad.",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 168,
            "NombrePlanEstudio": "Título de Experto en Gestión y Marketing de la Oficina de Farmacia",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3004,
            "NombrePlanEstudio": "Título de Experto en Helicopter Emergency Medical Service y Asistencia Médica Aerotransportada",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3024,
            "NombrePlanEstudio": "Título de Experto en Interiorismo de Espacios Comerciales y Residenciales",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 172,
            "NombrePlanEstudio": "Título de Experto en Marketing y Comunicación Política",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 4170,
            "NombrePlanEstudio": "Título de Experto en Marketing y Comunicación Política",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3029,
            "NombrePlanEstudio": "TÍTULO DE EXPERTO EN MEDIACIÓN Y RESOLUCIÓN DE CONFLICTOS",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 169,
            "NombrePlanEstudio": "Título de Experto en Medicina Integrada",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3025,
            "NombrePlanEstudio": "Título de Experto en Neuromodulación percutánea y Técnicas invasivas",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 173,
            "NombrePlanEstudio": "Título de Experto en Periodismo Deportivo",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3026,
            "NombrePlanEstudio": "Título de Experto en Reeducación del suelo pélvico. Aplicación ginecológica, urológica, obstétrica y coloproctológica",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3060,
            "NombrePlanEstudio": "Título de Experto Universitario en Cirugía Menor Ambulatoria",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3056,
            "NombrePlanEstudio": "Título de Experto Universitario en Derecho Sanitario Internacional",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        },
        {
            "IdPlanEstudioNK": 3059,
            "NombrePlanEstudio": "Título de Experto Universitario en Derecho Sanitario: Marco Profesional español e internacional",
            "IdTipoEstudioNK": 4,
            "NombreTipoEstudio": "Estudios propios",
            "TotalHitos": 0
        }
    ]


def obtenerAsignaturas(titulacion_codigo):
    if (int(titulacion_codigo) == 112):
        return obtener_asignatura_112()
    elif (int(titulacion_codigo) == 125):
        return obtener_asignatura_125()
    else:
        return []

def obtener_asignatura_112():
    return [
        {
            "IdAsignaturaNK": 100226,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "BIOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100226"
        },
        {
            "IdAsignaturaNK": 100227,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "ESTRUCTURA Y FUNCIÓN CUERPO HUMANO I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100227"
        },
        {
            "IdAsignaturaNK": 100224,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "MATEMÁTICAS Y ESTADÍSTICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100224"
        },
        {
            "IdAsignaturaNK": 100225,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "QUÍMICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100225"
        },
        {
            "IdAsignaturaNK": 100233,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "INTRODUCCIÓN A LA FARMACIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100233"
        },
        {
            "IdAsignaturaNK": 101448,
            "Creditos": 2,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "8",
            "NombreClaseAsignatura": "Curso de especialización",
            "CodigoClaseAsignatura": "8",
            "NombreAsignatura": "INTRODUCCIÓN A LA GESTIÓN Y MARKETING FARMACÉUTICO",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100230,
            "Creditos": 8,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "BIOQUÍMICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100230"
        },
        {
            "IdAsignaturaNK": 100232,
            "Creditos": 10,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "ESTRUCTURA Y FUNCIÓN CUERPO HUMANO II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100232"
        },
        {
            "IdAsignaturaNK": 100231,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "FÍSICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100231"
        },
        {
            "IdAsignaturaNK": 100234,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "HISTORIA DE LA CIENCIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100234"
        },
        {
            "IdAsignaturaNK": 100237,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "FISIOPATOLOGÍA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100237"
        },
        {
            "IdAsignaturaNK": 100236,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "QUÍMICA INORGÁNICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100236"
        },
        {
            "IdAsignaturaNK": 100240,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "TÉCNICAS ANALÍTICAS",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100240"
        },
        {
            "IdAsignaturaNK": 100243,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "MICROBIOLOGÍA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100243"
        },
        {
            "IdAsignaturaNK": 100246,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PARASITOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100246"
        },
        {
            "IdAsignaturaNK": 100235,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "FÍSICO QUÍMICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100235"
        },
        {
            "IdAsignaturaNK": 100242,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "QUÍMICA ORGÁNICA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100242"
        },
        {
            "IdAsignaturaNK": 100247,
            "Creditos": 4,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "MICROBIOLOGÍA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100247"
        },
        {
            "IdAsignaturaNK": 100238,
            "Creditos": 8,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "NUTRICIÓN",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100241,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "SISTEMAS DE CALIDAD DE LABORATORIO",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100241"
        },
        {
            "IdAsignaturaNK": 101449,
            "Creditos": 3.5,
            "IdPlanEstudioNK": 112,
            "Curso": "2",
            "IdClaseAsignaturaNK": "8",
            "NombreClaseAsignatura": "Curso de especialización",
            "CodigoClaseAsignatura": "8",
            "NombreAsignatura": "EL EQUIPO HUMANO EN LA FARMACIA: GESTIÓN DE LOS RECURSOS HUMANOS",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100248,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "QUÍMICA ORGÁNICA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100248"
        },
        {
            "IdAsignaturaNK": 100253,
            "Creditos": 7,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ANÁLISIS BIOLÓGICOS Y DE DIAGNÓSTICO DE LABORATORIO I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100253"
        },
        {
            "IdAsignaturaNK": 100250,
            "Creditos": 4,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "BIOFARMACIA Y FARMACOCINÉTICA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100250"
        },
        {
            "IdAsignaturaNK": 100257,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FARMACOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100257"
        },
        {
            "IdAsignaturaNK": 100252,
            "Creditos": 3,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FISIOPATOLOGÍA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100252"
        },
        {
            "IdAsignaturaNK": 100251,
            "Creditos": 4,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "INMUNOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100251"
        },
        {
            "IdAsignaturaNK": 100258,
            "Creditos": 8,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ANÁLISIS BIOLÓGICOS Y DE DIAGNÓSTICO DE LABORATORIO II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100258"
        },
        {
            "IdAsignaturaNK": 100256,
            "Creditos": 5,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "BIOFARMACIA Y FARMACOCINÉTICA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100256"
        },
        {
            "IdAsignaturaNK": 100254,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "BOTÁNICA FARMACÉUTICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100254"
        },
        {
            "IdAsignaturaNK": 100249,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "DOCTRINA SOCIAL DE LA IGLESIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100249"
        },
        {
            "IdAsignaturaNK": 100255,
            "Creditos": 5,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "TECNOLOGÍA FARMACÉUTICA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100255"
        },
        {
            "IdAsignaturaNK": 101450,
            "Creditos": 3.5,
            "IdPlanEstudioNK": 112,
            "Curso": "3",
            "IdClaseAsignaturaNK": "8",
            "NombreClaseAsignatura": "Curso de especialización",
            "CodigoClaseAsignatura": "8",
            "NombreAsignatura": "MARKETING FARMACÉUTICO",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100260,
            "Creditos": 7,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FARMACOGNOSIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100260"
        },
        {
            "IdAsignaturaNK": 100262,
            "Creditos": 7,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FARMACOLOGÍA Y FARMACIA CLÍNICA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100262"
        },
        {
            "IdAsignaturaNK": 100259,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "QUÍMICA FARMACÉUTICA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100259"
        },
        {
            "IdAsignaturaNK": 100263,
            "Creditos": 4,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "SALUD PÚBLICA ",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100263"
        },
        {
            "IdAsignaturaNK": 100261,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "TECNOLOGÍA FARMACÉUTICA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100261"
        },
        {
            "IdAsignaturaNK": 100267,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FARMACOLOGÍA Y FARMACIA CLÍNICA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100267"
        },
        {
            "IdAsignaturaNK": 100265,
            "Creditos": 3,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FITOTERAPIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100265"
        },
        {
            "IdAsignaturaNK": 100268,
            "Creditos": 3,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "HABILIDADES DE COMUNICACIÓN",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100268"
        },
        {
            "IdAsignaturaNK": 100264,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "QUÍMICA FARMACÉUTICA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100264"
        },
        {
            "IdAsignaturaNK": 100266,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "TECNOLOGÍA FARMACÉUTICA III",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100266"
        },
        {
            "IdAsignaturaNK": 100269,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "TOXICOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100269"
        },
        {
            "IdAsignaturaNK": 101451,
            "Creditos": 3.5,
            "IdPlanEstudioNK": 112,
            "Curso": "4",
            "IdClaseAsignaturaNK": "8",
            "NombreClaseAsignatura": "Curso de especialización",
            "CodigoClaseAsignatura": "8",
            "NombreAsignatura": "LOGÍSTICA, COMPRAS, VENTAS Y SERVICIOS",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100274,
            "Creditos": 4,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ATENCIÓN FARMACÉUTICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100274"
        },
        {
            "IdAsignaturaNK": 100270,
            "Creditos": 3.5,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "BIOTECNOLOGÍA FARMACÉUTICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100270"
        },
        {
            "IdAsignaturaNK": 100272,
            "Creditos": 4.5,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "GESTIÓN Y PLANIFICACIÓN",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100272"
        },
        {
            "IdAsignaturaNK": 100273,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "HISTORIA, LEGISLACIÓN Y DEONTOLOGÍA FARMACÉUTICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100273"
        },
        {
            "IdAsignaturaNK": 100271,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRODUCTOS SANITARIOS Y COSMÉTICOS",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100271"
        },
        {
            "IdAsignaturaNK": 100278,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "P",
            "NombreClaseAsignatura": "Optativa",
            "CodigoClaseAsignatura": "OP",
            "NombreAsignatura": "FARMACIA HOSPITALARIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100278"
        },
        {
            "IdAsignaturaNK": 100276,
            "Creditos": 24,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "1",
            "NombreClaseAsignatura": "Practicum",
            "CodigoClaseAsignatura": "P",
            "NombreAsignatura": "PRÁCTICAS TUTELADAS",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100276"
        },
        {
            "IdAsignaturaNK": 100275,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "3",
            "NombreClaseAsignatura": "Trabajo fin de Grado",
            "CodigoClaseAsignatura": "TFG",
            "NombreAsignatura": "TRABAJO FIN DE GRADO",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100275"
        },
        {
            "IdAsignaturaNK": 100279,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "P",
            "NombreClaseAsignatura": "Optativa",
            "CodigoClaseAsignatura": "OP",
            "NombreAsignatura": "FARMACOGENÉTICA Y FARMACOGENÓMICA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100277,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "P",
            "NombreClaseAsignatura": "Optativa",
            "CodigoClaseAsignatura": "OP",
            "NombreAsignatura": "METODOLOGÍA CIENTÍFICA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 101452,
            "Creditos": 5.5,
            "IdPlanEstudioNK": 112,
            "Curso": "5",
            "IdClaseAsignaturaNK": "8",
            "NombreClaseAsignatura": "Curso de especialización",
            "CodigoClaseAsignatura": "8",
            "NombreAsignatura": "GESTIÓN LEGAL Y ECONÓMICO-FINANCIERA DE UNA OFICINA DE FARMACIA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100229,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "ANTROPOLOGÍA FILOSÓFICA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100245,
            "Creditos": 3,
            "IdPlanEstudioNK": 112,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "BIOÉTICA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100244,
            "Creditos": 3,
            "IdPlanEstudioNK": 112,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "HISTORIA DE LA CIENCIA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100228,
            "Creditos": 6,
            "IdPlanEstudioNK": 112,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "SOCIEDAD E HISTORIA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        }
    ]

def obtener_asignatura_125():
    return [
        {
            "IdAsignaturaNK": 100289,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "ANATOMÍA E HISTOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100289"
        },
        {
            "IdAsignaturaNK": 100288,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "BIOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100288"
        },
        {
            "IdAsignaturaNK": 100291,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "BIOQUÍMICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100291"
        },
        {
            "IdAsignaturaNK": 100290,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "FISIOLOGÍA GENERAL",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100290"
        },
        {
            "IdAsignaturaNK": 100298,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "HISTORIA DE LA CIENCIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100298"
        },
        {
            "IdAsignaturaNK": 100294,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "ANATOMÍA ESPECIAL",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "co",
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100294"
        },
        {
            "IdAsignaturaNK": 100295,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "FISIOLOGÍA ESPECIAL PARA ODONTÓLOGOS",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100295"
        },
        {
            "IdAsignaturaNK": 100299,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "INTRODUCCIÓN A LA CLÍNICA ODONTOLÓGICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100299"
        },
        {
            "IdAsignaturaNK": 100300,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "PSICOLOGÍA ",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100300"
        },
        {
            "IdAsignaturaNK": 100293,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ESTADÍSTICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es",
                "xi"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100293"
        },
        {
            "IdAsignaturaNK": 100301,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "B",
            "NombreClaseAsignatura": "Formación Básica",
            "CodigoClaseAsignatura": "FB",
            "NombreAsignatura": "MICROBIOLOGÍA Y VIROLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100301"
        },
        {
            "IdAsignaturaNK": 100304,
            "Creditos": 4,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FARMACOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100304"
        },
        {
            "IdAsignaturaNK": 100302,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "FUNDAMENTOS FÍSICOS DE LA IMAGEN Y RADIOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100302"
        },
        {
            "IdAsignaturaNK": 100303,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "INTRODUCCIÓN A LA INVESTIGACIÓN",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100303"
        },
        {
            "IdAsignaturaNK": 100305,
            "Creditos": 2,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "NUTRICIÓN",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100305"
        },
        {
            "IdAsignaturaNK": 100306,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PATOLOGÍA GENERAL I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100306"
        },
        {
            "IdAsignaturaNK": 100309,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ANATOMÍA PATOLÓGICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100309"
        },
        {
            "IdAsignaturaNK": 100313,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "BIOMATERIALES E INSTRUMENTACIÓN",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100313"
        },
        {
            "IdAsignaturaNK": 100312,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "DOCTRINA SOCIAL DE LA IGLESIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100312"
        },
        {
            "IdAsignaturaNK": 100310,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "MANIFESTACIONES ORALES DE LA PATOLOGÍA SISTÉMICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100310"
        },
        {
            "IdAsignaturaNK": 100308,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PATOLOGÍA GENERAL II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100311,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "2",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PATOLOGÍA QUIRÚRGICA Y REANIMACIÓN",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100311"
        },
        {
            "IdAsignaturaNK": 100316,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "CIRUGÍA BUCAL I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100316"
        },
        {
            "IdAsignaturaNK": 100315,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "MEDICINA BUCAL I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100315"
        },
        {
            "IdAsignaturaNK": 100314,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ODONTOLOGÍA PREVENTIVA Y COMUNITARIA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100314"
        },
        {
            "IdAsignaturaNK": 100318,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PATOLOGÍA Y TERAPÉUTICA DENTAL I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100318"
        },
        {
            "IdAsignaturaNK": 100317,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRÓTESIS I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100317"
        },
        {
            "IdAsignaturaNK": 100322,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "CIRUGÍA BUCAL II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100322"
        },
        {
            "IdAsignaturaNK": 100321,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "MEDICINA BUCAL II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100321"
        },
        {
            "IdAsignaturaNK": 100324,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PATOLOGÍA Y TERAPÉUTICA DENTAL II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100324"
        },
        {
            "IdAsignaturaNK": 100323,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRÓTESIS II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100323"
        },
        {
            "IdAsignaturaNK": 100319,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "P",
            "NombreClaseAsignatura": "Optativa",
            "CodigoClaseAsignatura": "OP",
            "NombreAsignatura": "INGLÉS ",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100319"
        },
        {
            "IdAsignaturaNK": 100320,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "3",
            "IdClaseAsignaturaNK": "P",
            "NombreClaseAsignatura": "Optativa",
            "CodigoClaseAsignatura": "OP",
            "NombreAsignatura": "NUEVAS TECNOLOGÍAS ",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100320"
        },
        {
            "IdAsignaturaNK": 100325,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "EPIDEMIOLOGÍA Y SALUD PÚBLICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100325"
        },
        {
            "IdAsignaturaNK": 100326,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ODONTOPEDIATRÍA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100326"
        },
        {
            "IdAsignaturaNK": 100328,
            "Creditos": 4,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ORTODONCIA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100328"
        },
        {
            "IdAsignaturaNK": 100330,
            "Creditos": 5,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PATOLOGÍA Y TERAPÉUTICA DENTAL III",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100330"
        },
        {
            "IdAsignaturaNK": 100327,
            "Creditos": 4,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PERIODONCIA I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100327"
        },
        {
            "IdAsignaturaNK": 100329,
            "Creditos": 5,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRÓTESIS III",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100329"
        },
        {
            "IdAsignaturaNK": 100338,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ODONTOLOGÍA MÍNIMAMENTE INVASIVA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100338"
        },
        {
            "IdAsignaturaNK": 100331,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ODONTOPEDIATRÍA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100331"
        },
        {
            "IdAsignaturaNK": 100333,
            "Creditos": 4,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ORTODONCIA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100333"
        },
        {
            "IdAsignaturaNK": 100335,
            "Creditos": 5,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PATOLOGÍA Y TERAPÉUTICA DENTAL IV",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100335"
        },
        {
            "IdAsignaturaNK": 100332,
            "Creditos": 4,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PERIODONCIA II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100332"
        },
        {
            "IdAsignaturaNK": 100334,
            "Creditos": 5,
            "IdPlanEstudioNK": 125,
            "Curso": "4",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRÓTESIS IV",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100334"
        },
        {
            "IdAsignaturaNK": 100341,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "GERODONTOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100341"
        },
        {
            "IdAsignaturaNK": 100342,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "IMPLANTOLOGÍA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100342"
        },
        {
            "IdAsignaturaNK": 100340,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ODONTOLOGÍA PARA PACIENTES ESPECIALES",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100340"
        },
        {
            "IdAsignaturaNK": 100343,
            "Creditos": 4,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ORTODONCIA III",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100343"
        },
        {
            "IdAsignaturaNK": 100344,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRACTICUM ADULTOS I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100344"
        },
        {
            "IdAsignaturaNK": 100345,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRACTICUM INFANTIL I",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100345"
        },
        {
            "IdAsignaturaNK": 100346,
            "Creditos": 5,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "URGENCIAS Y FARMACOLOGÍA APLICADAS A LA PRÁCTICA ODONTOLÓGICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S1",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100346"
        },
        {
            "IdAsignaturaNK": 100339,
            "Creditos": 5,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ODONTOLOGÍA LEGAL Y PROTECCIÓN RADIOLOGICA",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100339"
        },
        {
            "IdAsignaturaNK": 100348,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ORGANIZACIÓN Y GESTIÓN DE LA CLÍNICA DENTAL",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100348"
        },
        {
            "IdAsignaturaNK": 100347,
            "Creditos": 4,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "ORTODONCIA IV",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100347"
        },
        {
            "IdAsignaturaNK": 100349,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRACTICUM ADULTOS II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100349"
        },
        {
            "IdAsignaturaNK": 100350,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PRACTICUM INFANTIL II",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100350"
        },
        {
            "IdAsignaturaNK": 100351,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "5",
            "IdClaseAsignaturaNK": "3",
            "NombreClaseAsignatura": "Trabajo fin de Grado",
            "CodigoClaseAsignatura": "TFG",
            "NombreAsignatura": "TRABAJO FIN DE GRADO",
            "Hitos": [],
            "PeriodosGrupo": [
            {
                "Periodo": "S2",
                "IdiomasGrupo": [
                "en",
                "es"
                ]
            }
            ],
            "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100351"
        },
        {
            "IdAsignaturaNK": 100292,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "ANTROPOLOGÍA FILOSÓFICA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100337,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "BIOÉTICA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100307,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "BIOMATERIALES Y ERGONOMÍA",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100336,
            "Creditos": 3,
            "IdPlanEstudioNK": 125,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "CIENCIA Y SOCIEDAD",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100296,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "HISTORIA GENERAL DE EUROPA Y DE LA CIVILIZACION OCCIDENTAL",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 100297,
            "Creditos": 6,
            "IdPlanEstudioNK": 125,
            "Curso": "",
            "IdClaseAsignaturaNK": " ",
            "NombreClaseAsignatura": "No informado",
            "CodigoClaseAsignatura": " ",
            "NombreAsignatura": "PSICOLOGÍA ",
            "Hitos": [],
            "PeriodosGrupo": [],
            "UrlGuiaDocente": ""
        }
    ]


def procesarCampus():
    # LOS CAMPUS SE CARGARAN MANUALMENTE PARA RESPETAR EL ID
    # campus = obtenerCampus()
    # for item in campus:
    #     camp = Campus.objects.filter(id=item['IdCampusNK'])
    #     if camp:
    #         camp = camp[0]
    #     else:
    #         camp = Campus.objects.filter(id=item['IdCampusNK']).first
    #         camp.id = item['IdCampusNK']
    #         camp.universidad = 1                 # cardenal herrera
    #         camp.nombre = item['NombreCampus']
    #         camp.save()
    #         print('Se agregó campus: ', item['NombreCampus'])
    pass


def procesarTitulaciones():
    titulaciones = obtenerTitulaciones()
    for titulacion in titulaciones:
        # "IdPlanEstudioNK": 130,
        # "NombrePlanEstudio": "Architecture (Grado en Fundamentos de Arquitectura)",
        # "IdTipoEstudioNK": 5,
        # "NombreTipoEstudio": "Grado",
        # "TotalHitos": 0    

        oTitulacion = grabarTitulacion(titulacion)
        procesarAsignaturas(oTitulacion.codigo)


def grabarTitulacion(item):
    # el tipo de titulación se crea manualmente para respetar el id
    try:
        tp = TipoTitulacion.objects.get(id=item['IdTipoEstudioNK'])
    except Exception as error:
        raise ValueError('No existe tipo de titulación: "{}" {}'.format(item['IdTipoEstudioNK'], item['NombreTipoEstudio']))

    tit = Titulacion.objects.filter(codigo=item['IdPlanEstudioNK'])
    if tit:
        tit = tit.first()
    else:
        tit = Titulacion.objects.create(tipo_titulacion_id = tp.id, codigo = item['IdPlanEstudioNK'], nombre = item['NombrePlanEstudio'])
        ti = TitulacionIdioma.objects.create(titulacion_id = tit.id, nombre = item['NombrePlanEstudio'], idioma = 'es')
        print('Se agregó titulación: {}'.format(item['NombrePlanEstudio']))

    return tit


def procesarAsignaturas(titulacion_codigo):
    plan_cc = ''
    curso_cc = ''
    asignaturas = obtenerAsignaturas(titulacion_codigo)
    for asignatura in asignaturas:
        # "IdAsignaturaNK": 100226,
        # "Creditos": 6,
        # "IdPlanEstudioNK": 112,
        # "Curso": "1",
        # "IdClaseAsignaturaNK": "B",
        # "NombreClaseAsignatura": "Formación Básica",
        # "CodigoClaseAsignatura": "FB",
        # "NombreAsignatura": "BIOLOGÍA",
        # "Hitos": [],
        # "PeriodosGrupo": [
        # {
        #     "Periodo": "S1",
        #     "IdiomasGrupo": [
        #     "en",
        #     "es"
        #     ]
        # }
        # ],
        # "UrlGuiaDocente": "https://gestionacademicavirtual.uchceu.es/doa/consultaPublica/look%5bconpub%5dMostrarPubGuiaDocAs?entradaPublica=true&_anoAcademico=2022&_codAsignatura=100226"
        
        if plan_cc != asignatura['IdPlanEstudioNK']:
            # comprobamos si existe plan de estudio para la titulación
            try:
                titulacion = Titulacion.objects.get(codigo=asignatura['IdPlanEstudioNK'])
            except Exception as error:
                raise ValueError('No existe titulación con código: {}'.format(asignatura['IdPlanEstudioNK']))
                
            oPlan = grabarPlanEstudio(titulacion, g_anyo_lectivo)
            plan_cc = asignatura['IdPlanEstudioNK']

        if curso_cc != asignatura['Curso']:
            oCurso = grabarCurso(asignatura, oPlan.id)
            curso_cc = asignatura['Curso']
        
        oAsignatura = grabarAsignatura(asignatura)
        oCursoAsignatura = grabarCursoAsignatura(oCurso, oAsignatura, asignatura)


def grabarPlanEstudio(titulacion, anyo):
    pe = PlanEstudio.objects.filter(titulacion_id=titulacion.id).filter(ciclo_lectivo=anyo)
    if pe:
        pe = pe.first()
    else:
        # creamos un plan de estudio para la titulación
        pe = PlanEstudio.objects.create(titulacion_id = titulacion.id, ciclo_lectivo = anyo)
        print('Se agregó plan de estudio {} para el ciclo lectivo {}'.format(titulacion.nombre, anyo))
    return pe


def grabarCurso(asignatura, plan_estudio_id):
    curso = Curso.objects.filter(plan_estudio_id=plan_estudio_id).filter(nombre='Curso {}'.format(asignatura['Curso']))
    if curso:
        curso = curso.first()
    else:
        curso = Curso.objects.create(plan_estudio_id=plan_estudio_id, nombre='Curso {}'.format(asignatura['Curso']))
        print('Se agregó curso: {}'.format(curso.nombre))
    return curso


def grabarAsignatura(item):
    asig = Asignatura.objects.filter(codigo=item['IdAsignaturaNK'])
    if asig:
        asig = asig.first()
    else:
        asig = Asignatura.objects.create(codigo=item['IdAsignaturaNK'], nombre=item['NombreAsignatura'], creditos=item['Creditos'])
        print('Se agregó asignatura: {}'.format(item['NombreAsignatura']))

        if len(item['PeriodosGrupo']) > 0 and len(item['PeriodosGrupo'][0]['IdiomasGrupo']) > 0:
            for i in range( len(item['PeriodosGrupo'][0]['IdiomasGrupo']) ):
                ai = AsignaturaIdioma.objects.create(asignatura_id=asig.id, idioma=item['PeriodosGrupo'][0]['IdiomasGrupo'][i], nombre=asig.nombre)
                print('Se agregó idioma {} para la asignatura {}'.format(ai.idioma, ai.nombre))
        else:
            ai = AsignaturaIdioma.objects.create(asignatura_id=asig.id, idioma='es', nombre=asig.nombre)                    
            print('Se agregó idioma {} para la asignatura {}'.format(ai.idioma, ai.nombre))
    return asig


def grabarCursoAsignatura(curso, asignatura, item):
    ca = CursoAsignatura.objects.filter(curso_id=curso.id).filter(asignatura_id=asignatura.id)
    if ca:
        ca = ca.first()
    else:
        ca = CursoAsignatura.objects.create(curso_id=curso.id, 
                                            asignatura_id=asignatura.id, 
                                            creditos=item['Creditos'], 
                                            tipo=item['CodigoClaseAsignatura'])
        if len(item['PeriodosGrupo']) > 0:
            ca.periodo = item['PeriodosGrupo'][0]['Periodo']
        ca.save()
        print('Se agregó curso-asignatura: {}'.format(ca.id))
    return ca


g_anyo_lectivo = 2021

if __name__ == "__main__":
    try:
        procesarTitulaciones()
    except Exception as error:
        print(repr(error))
