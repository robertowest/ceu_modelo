# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Areas(models.Model):
    facultad = models.ForeignKey('Facultades', models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=50)
    icono = models.CharField(max_length=25, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas'


class AreasTitulaciones(models.Model):
    area = models.ForeignKey(Areas, models.DO_NOTHING)
    titulacion = models.ForeignKey('Titulaciones', models.DO_NOTHING)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'areas_titulaciones'


class AsignaturaIdiomas(models.Model):
    asignatura = models.ForeignKey('Asignaturas', models.DO_NOTHING)
    nombre = models.CharField(max_length=160)
    idioma = models.CharField(max_length=2, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignatura_idiomas'
        unique_together = (('asignatura', 'idioma'),)


class Asignaturas(models.Model):
    nombre = models.CharField(max_length=160)
    creditos = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    citrix = models.CharField(max_length=5, blank=True, null=True)
    sigma = models.BigIntegerField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asignaturas'


class Campus(models.Model):
    universidad = models.ForeignKey('Universidades', models.DO_NOTHING)
    nombre = models.CharField(max_length=50)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus'


class CampusFacultad(models.Model):
    campus = models.ForeignKey(Campus, models.DO_NOTHING)
    facultad = models.ForeignKey('Facultades', models.DO_NOTHING)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_facultad'


class CampusTitulaciones(models.Model):
    campus = models.ForeignKey(Campus, models.DO_NOTHING)
    titulacion = models.ForeignKey('Titulaciones', models.DO_NOTHING)
    guid = models.CharField(unique=True, max_length=36, blank=True, null=True)
    plazas = models.SmallIntegerField(blank=True, null=True)
    url_calendario = models.CharField(max_length=160, blank=True, null=True)
    url_horario = models.CharField(max_length=160, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'campus_titulaciones'
        unique_together = (('campus', 'titulacion'),)


class Cursos(models.Model):
    plan_estudio = models.ForeignKey('PlanesEstudios', models.DO_NOTHING)
    curso = models.SmallIntegerField()
    nombre = models.CharField(max_length=50)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursos'


class CursosAsignaturas(models.Model):
    curso = models.ForeignKey(Cursos, models.DO_NOTHING)
    asignatura = models.ForeignKey(Asignaturas, models.DO_NOTHING)
    profesor = models.ForeignKey('Profesores', models.DO_NOTHING)
    periodo = models.CharField(max_length=2, blank=True, null=True)
    creditos = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)
    url_guia = models.CharField(max_length=160, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cursos_asignaturas'


class Departamento(models.Model):
    id = models.IntegerField()
    facultad = models.ForeignKey('Facultades', models.DO_NOTHING)
    nombre = models.CharField(max_length=120)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'


class Facultades(models.Model):
    nombre = models.CharField(max_length=80)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'facultades'


class Funciones(models.Model):
    nombre = models.CharField(max_length=150)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funciones'


class Jpa(models.Model):
    id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    fecha = models.DateField()
    tipo = models.CharField(max_length=1, blank=True, null=True)
    es_nacional = models.IntegerField()
    campus_id = models.IntegerField(blank=True, null=True)
    titulacion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jpa'


class JpaIdiomas(models.Model):
    id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    idioma = models.CharField(max_length=2, blank=True, null=True)
    jpa_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jpa_idiomas'


class Personas(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dni = models.CharField(max_length=9)
    sexo = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'


class PlanesEstudios(models.Model):
    titulacion = models.ForeignKey('Titulaciones', models.DO_NOTHING)
    ciclo_lectivo = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'planes_estudios'
        unique_together = (('titulacion', 'ciclo_lectivo'),)


class Profesores(models.Model):
    persona = models.ForeignKey(Personas, models.DO_NOTHING)
    foto = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesores'


class ProfesoresFunciones(models.Model):
    profesor = models.ForeignKey(Profesores, models.DO_NOTHING)
    funcion = models.ForeignKey(Funciones, models.DO_NOTHING)
    prioridad = models.SmallIntegerField(blank=True, null=True)
    principal = models.IntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profesores_funciones'
        unique_together = (('profesor', 'funcion'), ('profesor', 'principal'),)


class TiposTitulaciones(models.Model):
    nombre = models.CharField(max_length=50)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipos_titulaciones'


class TitulacionAux(models.Model):
    id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    tipo_encabezado = models.CharField(max_length=1)
    url_imagen_1 = models.CharField(max_length=160)
    text_imagen_1 = models.CharField(max_length=160)
    subtext_imagen_1 = models.CharField(max_length=160)
    url_imagen_2 = models.CharField(max_length=160, blank=True, null=True)
    text_imagen_2 = models.CharField(max_length=160, blank=True, null=True)
    subtext_imagen_2 = models.CharField(max_length=160, blank=True, null=True)
    url_imagen_3 = models.CharField(max_length=160, blank=True, null=True)
    text_imagen_3 = models.CharField(max_length=160, blank=True, null=True)
    subtext_imagen_3 = models.CharField(max_length=160, blank=True, null=True)
    titulacion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulacion_aux'


class TitulacionHtml(models.Model):
    id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    grupo = models.CharField(max_length=80, blank=True, null=True)
    titulo = models.CharField(max_length=80, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    titulacion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulacion_html'


class TitulacionIdiomas(models.Model):
    titulacion = models.ForeignKey('Titulaciones', models.DO_NOTHING)
    nombre = models.CharField(max_length=160)
    idioma = models.CharField(max_length=2, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=150, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulacion_idiomas'
        unique_together = (('titulacion', 'idioma'),)


class TitulacionUrl(models.Model):
    id = models.IntegerField()
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField()
    grupo = models.CharField(max_length=80, blank=True, null=True)
    url = models.CharField(max_length=180, blank=True, null=True)
    texto = models.CharField(max_length=80, blank=True, null=True)
    titulacion_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulacion_url'


class Titulaciones(models.Model):
    tipo_titulacion = models.ForeignKey(TiposTitulaciones, models.DO_NOTHING)
    nombre = models.CharField(max_length=160)
    duracion = models.IntegerField(blank=True, null=True)
    duracion_tipo = models.CharField(max_length=1, blank=True, null=True)
    creditos = models.SmallIntegerField(blank=True, null=True)
    modalidad = models.CharField(max_length=1, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=150, blank=True, null=True)
    citrix = models.CharField(max_length=5, blank=True, null=True)
    sigma = models.BigIntegerField(blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'titulaciones'


class Universidades(models.Model):
    nombre = models.CharField(max_length=50)
    created_on = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universidades'
