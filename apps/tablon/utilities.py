import json
import requests


def srvDESA():
    return 'http://desa01.ceu.es/Webservices/Uch/WebApiPlanesEstudiosWeb/api'


def srvPROD():
    return 'https://services.ceu.es/Webservices/Uch/WebApiPlanesEstudiosWeb/api'


def obtenerCampus():
    resp = requests.get('{0}/Campus'.format(srvPROD()))
    return resp


def obtenerTipoTitulaciones():
    corte = ""
    resp = []
    titulaciones = obtenerTitulaciones();
    for titulacion in titulaciones:
        if titulacion['NombreTipoEstudio'] != corte:
            corte = titulacion['NombreTipoEstudio']
            resp.append( {'NombreTipoEstudio': titulacion['NombreTipoEstudio']} )
    return resp

    
def obtenerTitulaciones():
    # resp = requests.get('{0}/PlanesEstudios?soloGradosPostgrados=true&soloPlanesConHitos=false'.format(srvPROD()))
    resp = [
        {
            "IdPlanEstudioNK": 130,
            "NombrePlanEstudio": "Architecture (Grado en Fundamentos de Arquitectura)",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 135,
            "NombrePlanEstudio": "Doble Grado Derecho y Ciencias Políticas y de la Administración",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 150,
            "NombrePlanEstudio": "Doble Grado Educación Infantil y Educación Primaria",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 151,
            "NombrePlanEstudio": "Doble Grado Educación Primaria y Educación Infantil",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 182,
            "NombrePlanEstudio": "Doble Grado en Ciencias de la Actividad Física y el Deporte + Educación Primaria",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 140,
            "NombrePlanEstudio": "Doble Grado en Ciencias Políticas / Relaciones Internacionales + Periodismo",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 141,
            "NombrePlanEstudio": "Doble Grado en Ciencias Políticas y de la Administración y Dirección de Empresas",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 139,
            "NombrePlanEstudio": "Doble Grado en Ciencias Políticas/Relaciones Internacionales + Publicidad y Relaciones Públicas",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 148,
            "NombrePlanEstudio": "Doble Grado en Comunicación Audiovisual + Periodismo",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 149,
            "NombrePlanEstudio": "Doble Grado en Comunicación Audiovisual + Publicidad y Relaciones Públicas",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 137,
            "NombrePlanEstudio": "Doble Grado en Derecho + Publicidad y Relaciones Públicas",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 136,
            "NombrePlanEstudio": "Doble Grado en Derecho y Dirección de Empresas",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 174,
            "NombrePlanEstudio": "Doble Grado en Dirección de Empresas y Derecho",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 138,
            "NombrePlanEstudio": "Doble Grado en Dirección de Empresas y Marketing",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 179,
            "NombrePlanEstudio": "Doble Grado en Dirección de Empresas y Título de Especialista en Dirección y Gestión Deportiva",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 176,
            "NombrePlanEstudio": "Doble Grado en Farmacia y Nutrición Humana y Dietética",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 175,
            "NombrePlanEstudio": "Doble Grado en Marketing y Publicidad y RR.PP.",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 142,
            "NombrePlanEstudio": "Doble Grado en Periodismo + Ciencias Políticas / Relaciones Internacionales",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 147,
            "NombrePlanEstudio": "Doble Grado en Periodismo + Comunicación Audiovisual",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 146,
            "NombrePlanEstudio": "Doble Grado en Periodismo + Publicidad y Relaciones Públicas",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 145,
            "NombrePlanEstudio": "Doble Grado en Publicidad y Relaciones Públicas + Comunicación Audiovisual",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 143,
            "NombrePlanEstudio": "Doble Grado en Publicidad y Relaciones Públicas + Marketing",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 144,
            "NombrePlanEstudio": "Doble Grado en Publicidad y Relaciones Públicas + Periodismo",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 152,
            "NombrePlanEstudio": "Doble Grado Fisioterapia y Enfermería",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 123,
            "NombrePlanEstudio": "Grado en Arquitectura (Architecture)",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 181,
            "NombrePlanEstudio": "Grado en Ciencias de la Actividad Física y el Deporte",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 126,
            "NombrePlanEstudio": "GRADO EN CIENCIAS POLÍTICAS",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 165,
            "NombrePlanEstudio": "Grado en Ciencias Políticas + Título de Experto en Marketing y Comunicación Política",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 110,
            "NombrePlanEstudio": "Grado en Comunicación Audiovisual",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 157,
            "NombrePlanEstudio": "Grado en Comunicación Audiovisual + Título de Especialista en Comunicación de Moda",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 121,
            "NombrePlanEstudio": "Grado en Derecho",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 156,
            "NombrePlanEstudio": "Grado en Derecho + Título de Especialista en Derecho Internacional y Derecho Europeo",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 166,
            "NombrePlanEstudio": "Grado en Derecho + Título de Especialista en Integración Europea y Mercado Exterior",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 119,
            "NombrePlanEstudio": "GRADO EN DIRECCIÓN DE EMPRESAS",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 161,
            "NombrePlanEstudio": "Grado en Dirección de Empresas + Título de Especialista en Integración Europea y Mercado Exterior",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 127,
            "NombrePlanEstudio": "Grado en Educación Infantil",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 128,
            "NombrePlanEstudio": "Grado en Educación Primaria",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 111,
            "NombrePlanEstudio": "GRADO EN ENFERMERÍA",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 112,
            "NombrePlanEstudio": "GRADO EN FARMACIA",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 153,
            "NombrePlanEstudio": "Grado en Farmacia + Título Experto Gestión y Marketing de la oficina de Farmacia",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 113,
            "NombrePlanEstudio": "GRADO EN FISIOTERAPIA",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 120,
            "NombrePlanEstudio": "GRADO EN INGENIERÍA EN DISEÑO INDUSTRIAL Y DESARROLLO DE PRODUCTOS",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 129,
            "NombrePlanEstudio": "Grado en Marketing",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 162,
            "NombrePlanEstudio": "Grado en Marketing + Título de Especialista en Integración Europea y Mercado Exterior",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 124,
            "NombrePlanEstudio": "Grado en Medicina",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 164,
            "NombrePlanEstudio": "Grado en Medicina + Título de Experto en Medicina Integrada",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 134,
            "NombrePlanEstudio": "Grado en Nutrición Humana y Dietética (Plan/2016)",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 125,
            "NombrePlanEstudio": "GRADO EN ODONTOLOGÍA",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 131,
            "NombrePlanEstudio": "Grado en Óptica y Optometría",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 117,
            "NombrePlanEstudio": "Grado en Periodismo",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 160,
            "NombrePlanEstudio": "Grado en Periodismo + Título de Especialista en Comunicación de Moda",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 154,
            "NombrePlanEstudio": "Grado en Periodismo + Título de Experto en Periodismo Deportivo",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 159,
            "NombrePlanEstudio": "Grado en Periodismo + Título Experto en Marketing y Comunicación Política",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 155,
            "NombrePlanEstudio": "Grado en Publicidad + Título Experto en Marketing y Comunicación Política",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 118,
            "NombrePlanEstudio": "Grado en Publicidad y Relaciones Públicas",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 163,
            "NombrePlanEstudio": "Grado en Publicidad y RRPP + Título de Especialista en Comunicación de Moda",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 122,
            "NombrePlanEstudio": "GRADO EN VETERINARIA",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 132,
            "NombrePlanEstudio": "Graduado/a en Gastronomía/Gastronomy",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 1,
            "NombrePlanEstudio": "Plan de Estudios de Movilidad",
            "NombreTipoEstudio": "Grado",
        },
        {
            "IdPlanEstudioNK": 2014,
            "NombrePlanEstudio": "M.U. en Gestión de Instalaciones Energéticas e Internacionalización de Proyectos",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2003,
            "NombrePlanEstudio": "Máster UNIVERSITARIO DE ESPECIALIZACIÓN EN CUIDADOS DE ENFERMERÍA",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2011,
            "NombrePlanEstudio": "Máster Universitario en Abogacía",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2020,
            "NombrePlanEstudio": "Máster Universitario en Abogacía + Máster Propio en Derecho Internacional de los Negocios",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2022,
            "NombrePlanEstudio": "Máster Universitario en Arquitectura",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2004,
            "NombrePlanEstudio": "Máster Universitario en Comunicación Y Branding Digital",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2009,
            "NombrePlanEstudio": "Máster Universitario en Diseño de Interiores",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2017,
            "NombrePlanEstudio": "Máster Universitario en Diseño de Producto",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2016,
            "NombrePlanEstudio": "Máster Universitario en Diseño y Comunicación Gráfica",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2013,
            "NombrePlanEstudio": "Máster Universitario en Educación Bilingüe (Inglés y Español)",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2018,
            "NombrePlanEstudio": "Máster Universitario en Fisioterapia Deportiva",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2001,
            "NombrePlanEstudio": "Máster Universitario en Formación del Profesorado de Educación Secundaria Obligatoria y Bachillerato, Formación Profesional y Enseñanzas de Idiomas",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2012,
            "NombrePlanEstudio": "Máster Universitario en Gestión Ambiental",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2010,
            "NombrePlanEstudio": "Máster Universitario en Gestión de Proyectos e Instalaciones Energéticas",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2007,
            "NombrePlanEstudio": "Máster Universitario en Gestión y Dirección de Centros Educativos",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2019,
            "NombrePlanEstudio": "Máster Universitario en Psicología General Sanitaria",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2021,
            "NombrePlanEstudio": "Máster Universitario en Psicología Jurídica y Práctica Forense",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2008,
            "NombrePlanEstudio": "Máster Universitario en Seguridad Alimentaria",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 2015,
            "NombrePlanEstudio": "Máster Universitario en Técnicas Avanzadas Estéticas y Láser",
            "NombreTipoEstudio": "Máster Universitario",
        },
        {
            "IdPlanEstudioNK": 3012,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Animales Exóticos",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3006,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Cirugía de Tejidos Blandos en Pequeños Animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3071,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Cirugía en Pequeños Animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3013,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Dermatología de Pequeños animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3005,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Diagnóstico por Imagen en Pequeños Animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3010,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Medicina felina",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3008,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Medicina Interna de Pequeños Animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4008,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Medicina Interna y Urgencias en Pequeños Animales.",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3011,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Neurología en Pequeños Animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3009,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Oftalmología de Pequeños Animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3007,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Traumatología en Pequeños Animales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4007,
            "NombrePlanEstudio": "Curso Superior de Posgrado en Traumatología y Ortopedia. Sistemas de Fijación externa en Pequeños Animales.",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3002,
            "NombrePlanEstudio": "Curso Superior En Audiología Protésica",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3021,
            "NombrePlanEstudio": "Curso Superior en Gestión de Riesgos y Seguros",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3065,
            "NombrePlanEstudio": "Curso Universitario en Mediación Civil y Mercantil",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4171,
            "NombrePlanEstudio": "Diploma Universitario de Especialización en Comunicación de Moda",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4180,
            "NombrePlanEstudio": "Diploma Universitario de Especialización en Derecho Internacional y Derecho Europeo",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4060,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Cirugía Menor Ambulatoria",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3066,
            "NombrePlanEstudio": "Diploma Universitario de experto en Derecho del Arte",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4178,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Dirección y Gestión Deportiva",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4022,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Diseño de Producto para el Hábitat",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4023,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Diseño Gráfico y Comunicación",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4001,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Ecografía Músculo-esquelética",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4018,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Enseñanza Escolar de la Religión Católica",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4168,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Gestión de Oficina de Farmacia y Marketing Farmacéutico",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4004,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Helicopter Emergency Medical Service y Asistencia Médica Aerotransportada",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4065,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Mediación Civil y Mercantil",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4029,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Mediación y Resolución de Conflictos",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4025,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Neuromodulación Percutánea y Técnicas Invasivas",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4173,
            "NombrePlanEstudio": "DIPLOMA UNIVERSITARIO DE EXPERTO EN PERIODISMO DEPORTIVO",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4026,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Reeducación del Suelo Pélvico. Aplicación Ginecológica, Urológica, Obstétrica y Coloproctológica",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4064,
            "NombrePlanEstudio": "Diploma Universitario de Experto en Showrunner en Ficción Audiovisual: Guión, Dirección y Producción de Series",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4172,
            "NombrePlanEstudio": "DIPLOMA UNIVERSITARIO DE FORMACIÓN AVANZADA EN FISIOTERAPIA ONCOLÓGICA",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3063,
            "NombrePlanEstudio": "European Master in Consumer Relationship Management",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3061,
            "NombrePlanEstudio": "M.P. en Cirugía Bucal e Implantología Bucofacial",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4182,
            "NombrePlanEstudio": "Máster de Formación Permanente en Cirugía Bucal ",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4063,
            "NombrePlanEstudio": "Máster de Formación Permanente en Customer Relationship Marketing",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4052,
            "NombrePlanEstudio": "Máster de Formación Permanente en Derecho Internacional de los Negocios",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4050,
            "NombrePlanEstudio": "Máster de Formación Permanente en Dirección Bursátil y Financiera",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4003,
            "NombrePlanEstudio": "Máster de Formación Permanente en Dirección y Monitorización de Ensayos Clínicos",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4051,
            "NombrePlanEstudio": "Máster de Formación Permanente en Especialización en Odontología Multidisciplinar Avanzada",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4016,
            "NombrePlanEstudio": "Máster de Formación Permanente en Especialización en Ortodoncia",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4053,
            "NombrePlanEstudio": "Máster de Formación Permanente en Especialización en Prótesis Avanzada",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4014,
            "NombrePlanEstudio": "Máster de Formación Permanente en Odontopediatría Integral",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4184,
            "NombrePlanEstudio": "Máster en Formación Permanente en Endodoncia/Master's Degree in Endodontics",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4017,
            "NombrePlanEstudio": "Máster en Formación Permanente en Odontología Conservadora y Endodoncia",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3057,
            "NombrePlanEstudio": "Master Program in Reasoning and Clinical practice for Physiotherapy",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3050,
            "NombrePlanEstudio": "Máster Propio Bursátil y Financiero",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3058,
            "NombrePlanEstudio": "MÁSTER PROPIO EN COMERCIO INTERNACIONAL Y NEGOCIO DIGITAL",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3054,
            "NombrePlanEstudio": "Máster Propio en Comunicación y Marketing Digital",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3052,
            "NombrePlanEstudio": "MÁSTER PROPIO EN DERECHO INTERNACIONAL DE LOS NEGOCIOS",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3003,
            "NombrePlanEstudio": "Máster Propio en Dirección y Monitorización de Ensayos Clínicos",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3051,
            "NombrePlanEstudio": "MÁSTER PROPIO EN ESPECIALIZACIÓN EN ODONTOLOGÍA MULTIDISCIPLINAR AVANZADA",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3016,
            "NombrePlanEstudio": "Máster Propio en Especialización en Ortodoncia",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3053,
            "NombrePlanEstudio": "Máster Propio en Especialización en Prótesis Avanzada",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3015,
            "NombrePlanEstudio": "Máster Propio en Implantología Oral",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3048,
            "NombrePlanEstudio": "Máster Propio en Neurociencias: cuidados médico-quirúrgicos y rehabilitación del paciente neurológico",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3017,
            "NombrePlanEstudio": "Máster Propio en Odontología Conservadora y Endodoncia",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3014,
            "NombrePlanEstudio": "Máster Propio en Odontopediatría",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3067,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Claves para el Diseño y la Arquitectura.",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 5171,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Comunicación de Moda",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4110,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Derecho Europeo",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4109,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Derecho Internacional",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4112,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Dirección Deportiva",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4021,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Gestión de Riesgos y Seguros",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4111,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Gestión Deportiva",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4024,
            "NombrePlanEstudio": "Programa de Formación Avanzada en Interiorismo de Espacios Comerciales y Residenciales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3062,
            "NombrePlanEstudio": "Programa Empleabilidad Integral del Maestro",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 171,
            "NombrePlanEstudio": "Título de Especialista en Comunicación de Moda",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 180,
            "NombrePlanEstudio": "Título de Especialista en Derecho Internacional y Derecho Europeo",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 178,
            "NombrePlanEstudio": "Título de Especialista en Dirección y Gestión Deportiva",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 167,
            "NombrePlanEstudio": "Título de Especialista en Integración Europea y Mercado Exterior",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3022,
            "NombrePlanEstudio": "Titulo de Experto en Diseño de Producto para el Hábitat",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3023,
            "NombrePlanEstudio": "Título de Experto en Diseño Gráfico y Comunicación",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3001,
            "NombrePlanEstudio": "Título de Experto en Ecografía Músculo-esquelética",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3018,
            "NombrePlanEstudio": "Título de Experto en Enseñanza Escolar de la Religión Católica",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3028,
            "NombrePlanEstudio": "Título de Experto en Estatuto Jurídico del Menor. Coordinador de Parentalidad.",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 168,
            "NombrePlanEstudio": "Título de Experto en Gestión y Marketing de la Oficina de Farmacia",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3004,
            "NombrePlanEstudio": "Título de Experto en Helicopter Emergency Medical Service y Asistencia Médica Aerotransportada",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3024,
            "NombrePlanEstudio": "Título de Experto en Interiorismo de Espacios Comerciales y Residenciales",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 172,
            "NombrePlanEstudio": "Título de Experto en Marketing y Comunicación Política",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 4170,
            "NombrePlanEstudio": "Título de Experto en Marketing y Comunicación Política",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3029,
            "NombrePlanEstudio": "TÍTULO DE EXPERTO EN MEDIACIÓN Y RESOLUCIÓN DE CONFLICTOS",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 169,
            "NombrePlanEstudio": "Título de Experto en Medicina Integrada",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3025,
            "NombrePlanEstudio": "Título de Experto en Neuromodulación percutánea y Técnicas invasivas",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 173,
            "NombrePlanEstudio": "Título de Experto en Periodismo Deportivo",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3026,
            "NombrePlanEstudio": "Título de Experto en Reeducación del suelo pélvico. Aplicación ginecológica, urológica, obstétrica y coloproctológica",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3060,
            "NombrePlanEstudio": "Título de Experto Universitario en Cirugía Menor Ambulatoria",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3056,
            "NombrePlanEstudio": "Título de Experto Universitario en Derecho Sanitario Internacional",
            "NombreTipoEstudio": "Estudios propios",
        },
        {
            "IdPlanEstudioNK": 3059,
            "NombrePlanEstudio": "Título de Experto Universitario en Derecho Sanitario: Marco Profesional español e internacional",
            "NombreTipoEstudio": "Estudios propios",
        }        
    ]
    return resp


def obtenerAsignaturas(plan_id):
    # resp = requests.get('{0}/PlanesEstudios/v2/{1}?incluirPeriodos=false&incluirIdiomas=false&incluirHitos=false'.format(srvPROD(), plan_id))
    resp = [
        {
            "IdAsignaturaNK": 102273,
            "Creditos": 1,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Arbitraje",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102283,
            "Creditos": 0.5,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "COMPETENCIA JUDICIAL INTERNACIONAL Y DERECHO APLICABLE",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102266,
            "Creditos": 2,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Deontología Profesional",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102270,
            "Creditos": 2,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Gestión de Despachos",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102268,
            "Creditos": 1.5,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Justicia Gratuita",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102274,
            "Creditos": 2,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Mediación",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102269,
            "Creditos": 1.5,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Organización Colegial",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102279,
            "Creditos": 4,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica Administrativa y Fiscal. Aspectos procesales",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102280,
            "Creditos": 3,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica Administrativa y Fiscal: Aspectos Sustantivos",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102275,
            "Creditos": 10,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica Civil y Mercantil: Aspectos Prácticos Procesales",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102276,
            "Creditos": 9,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica Civil y Mercantil: Aspectos Sustantivos",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102281,
            "Creditos": 3,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica laboral y de la S.s.: Aspectos Procesales",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102282,
            "Creditos": 2,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica laboral y de la S.s.: Aspectos Sustantivos",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102277,
            "Creditos": 7,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica Penal: Aspectos Prácticos Procesales",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102278,
            "Creditos": 1,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Práctica Penal: Aspectos Sustantivos",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102284,
            "Creditos": 0.5,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PROCEDIMIENTOS ANTE EL TRIBUNAL CONSTITUCIONAL",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102286,
            "Creditos": 0.5,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "PROCEDIMIENTOS ANTE TRIBUNALES EUROPEOS E INTERNACIONALES",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102271,
            "Creditos": 1,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Responsabilidad Civil y Penal de Los Abogados",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102272,
            "Creditos": 1,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Sistemas Alternativos De Resolución De Conflictos",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102267,
            "Creditos": 1,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "Turno de Oficio",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102285,
            "Creditos": 0.5,
            "IdPlanEstudioNK": 2011,
            "Curso": "1",
            "IdClaseAsignaturaNK": "O",
            "NombreClaseAsignatura": "Obligatoria",
            "CodigoClaseAsignatura": "OB",
            "NombreAsignatura": "VALIDEZ EXTRATERRITORIAL DE DECISIOINES",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102287,
            "Creditos": 30,
            "IdPlanEstudioNK": 2011,
            "Curso": "2",
            "IdClaseAsignaturaNK": "E",
            "NombreClaseAsignatura": "Prácticas externas",
            "CodigoClaseAsignatura": "PE",
            "NombreAsignatura": "Prácticas Externas",
            "UrlGuiaDocente": ""
        },
        {
            "IdAsignaturaNK": 102288,
            "Creditos": 6,
            "IdPlanEstudioNK": 2011,
            "Curso": "2",
            "IdClaseAsignaturaNK": "6",
            "NombreClaseAsignatura": "Trabajo fin de máster",
            "CodigoClaseAsignatura": "TFM",
            "NombreAsignatura": "TRABAJO FIN DE MASTER",
            "UrlGuiaDocente": ""
        }
    ]
    # titulaciones = obtenerTitulaciones();
    # for titulacion in titulaciones:
    #     if titulacion['NombreTipoEstudio'] != tipo_titulacion:
    #         resp.append( {'IdPlanEstudioNK': titulacion['IdPlanEstudioNK'], 
    #                       'NombrePlanEstudio': titulacion['NombrePlanEstudio'], 
    #                       'NombreTipoEstudio': titulacion['NombreTipoEstudio']} )
    return resp
