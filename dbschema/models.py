from django.db import models
from django.utils.html import mark_safe


class Universidad(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'ceu_universidades'
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'

    def __str__(self):
        return self.nombre
    

class Campus(models.Model):
    universidad = models.ForeignKey(Universidad, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'ceu_campus'
        verbose_name = 'Campus'
        verbose_name_plural = 'Cumpus'

    def __str__(self):
        return self.nombre


class Area(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'ceu_areas'
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.nombre


class TipoTitulacion(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_tipos_titulaciones'
        verbose_name = 'Tipo de Titulación'
        verbose_name_plural = 'Tipos de Titulaciones'

    def __str__(self):
        return self.nombre


class Titulacion(models.Model):
    tipo_titulacion = models.ForeignKey(TipoTitulacion, models.DO_NOTHING, blank=True, null=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    duracion_tipo = models.CharField(max_length=1, blank=True, null=True)
    codigo = models.CharField(max_length=8)
    nombre = models.CharField(max_length=160)
    creditos = models.SmallIntegerField(blank=True, null=True)
    insercion_laboral = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_titulaciones'
        verbose_name = 'Titulación'
        verbose_name_plural = 'Titulaciones'

    def __str__(self):
        return self.nombre


class TitulacionIdioma(models.Model):
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=160)
    idioma = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        db_table = 'ceu_titulacion_idiomas'
        verbose_name = 'Titulación Idioma'
        verbose_name_plural = 'Titulación Idiomas'

    def __str__(self):
        return self.nombre


class Competencia(models.Model):
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    grupo = models.CharField(max_length=30, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_competencias'
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competancias'


class SalidaProfesional(models.Model):
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    grupo = models.CharField(max_length=60, blank=True, null=True)
    texto = models.TextField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_salidas_profesionales'
        verbose_name = 'Salida Profesional'
        verbose_name_plural = 'Salidas Profesionales'


class PlanEstudio(models.Model):
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    ciclo_lectivo = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_planes_estudios'
        verbose_name = 'Plan de Estudio'
        verbose_name_plural = 'Planes de Estudios'

    def __str__(self):
        return '{} - {}'.format(self.ciclo_lectivo, self.titulacion.nombre)


class Curso(models.Model):
    plan_estudio = models.ForeignKey(PlanEstudio, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'ceu_cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return '{} - {}'.format(self.plan_estudio.nombre, self.nombre)


class Asignatura(models.Model):
    codigo = models.CharField(max_length=9, blank=True, null=True)
    nombre = models.CharField(max_length=160)
    creditos = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_asignaturas'
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def __str__(self):
        return self.nombre


class AsignaturaIdioma(models.Model):
    asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, blank=True, null=True)
    idioma = models.CharField(max_length=2, blank=True, null=True)
    nombre = models.CharField(max_length=160)

    class Meta:
        # managed = False
        db_table = 'ceu_asignatura_idiomas'
        verbose_name = 'Asignatura Idioma'
        verbose_name_plural = 'Asignatura Idiomas'

    def __str__(self):
        return self.nombre
    

class Persona(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return '{}, {}'.format(self.apellidos, self.nombre)
    

class Profesor(models.Model):
    # persona = models.ForeignKey(Persona, models.DO_NOTHING, blank=True, null=True)
    persona = models.OneToOneField(Persona, on_delete=models.DO_NOTHING)
    foto = models.ImageField(upload_to='profesor/foto/', blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_profesores'
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'

    def __str__(self):
        return '{} {}'.format(self.persona.nombre, self.persona.apellidos)

    @property
    def foto_preview(self):
        if self.foto:
            return mark_safe('<img src="{}" width="200" height="200" />'.format(self.foto.url))
        return ''
    

class Funcion(models.Model):
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=80)
    # principal = models.IntegerField(blank=True, null=True)
    PRINCIPAL = ( (True, 'Sí'), (False, 'No') )
    principal = models.BooleanField(default=False, choices=PRINCIPAL, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_funciones'
        verbose_name = 'Función'
        verbose_name_plural = 'Funciones'

    def __str__(self):
        return self.nombre
    

class CampusTitulacion(models.Model):
    campus = models.ForeignKey(Campus, models.DO_NOTHING, blank=True, null=True)
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    codigo = models.CharField(max_length=5)
    guid = models.CharField(max_length=36)
    plazas = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_campus_titulaciones'
        verbose_name = 'Cumpus Titulación'
        verbose_name_plural = 'Cumpus Titulaciones'

    def __str__(self):
        return '{} / {}'.format(self.campus.nombre, self.titulacion.nombre)
    

class CursoAsignatura(models.Model):
    curso_id = models.IntegerField(blank=True, null=True)
    asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, blank=True, null=True)
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING, blank=True, null=True)
    periodo = models.CharField(max_length=2, blank=True, null=True)     # T Trimestre / C Cuatrimestre / S Semestre
    creditos = models.SmallIntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True)        # FB Formación básica / OB Obligatoria / OP Optativa / PR Práctica / TFG Trabajo fin de grado

    class Meta:
        # managed = False
        db_table = 'ceu_cursos_asignaturas'
        verbose_name = 'Curso Asignatura'
        verbose_name_plural = 'Cursos Asignaturas'

    def __str__(self):
        return '{} / {}'.format(self.asignatura, self.profesor)
