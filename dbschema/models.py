from email.policy import default
from tabnanny import verbose
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe
from django.utils.translation import ugettext_lazy as _

from ckeditor.fields import RichTextField


class Auditable(models.Model):
    created_on = models.DateTimeField('Creado', auto_now_add=True, editable=False, null=True, blank=True)
    updated_on = models.DateTimeField('Modificado', auto_now=True, editable=False, null=True, blank=True)
    is_deleted = models.BooleanField('Eliminado', default=False)

    exclude_fields = ['created_on', 'updated_on']

    success_create_message = _('Registro creado correctamente')
    success_update_message = _('Registro actualizado correctamente')
    success_delete_message = _('Registro eliminado correctamente')

    error_create_message = _('El registro no pudo ser creado')
    error_update_message = _('El registro no pudo ser modificado')
    error_delete_message = _('El registro no pudo ser eliminado')

    not_found_message = _('No se ha encontrado un registro con estos datos')

    class Meta:
        abstract = True

    # TODO: no logro obtener los campos desde el objeto
    # def get_fields(self):
    #     # exclude = self.exclude_fields.append('active')
    #     # include = [f.name for f in self._meta.get_fields()
    #     #             if f.name not in self.exclude_fields]
    #     # return include.append('active')

    def get_data(self):
        '''Devuelve una lista con los nombres de todos los campos'''
        fields = []
        for f in self._meta.fields:
            # comprobamos que el campo sea del tipo que queremos visualizar
            # if f.editable and f.name not in self.exclude_fields:
            if f.editable and f.name:
                try:
                    value = getattr(self, f.name)
                    if value:
                        if f.choices:
                            fields.append({'name':f.verbose_name, 'value':dict(f.choices)[value],})
                        else:
                            fields.append({'name':f.verbose_name, 'value':value,})
                except:
                    value = None
        return fields

    def get_absolute_url(self):
        try:
            return reverse('%s:list' % self._meta.model_name)
        except:
            return reverse('%s:list' % self._meta.app_label)

    def get_list_url(self):
        return self.get_absolute_url()

    def get_detail_url(self):
        try:
            return reverse('%s:detail' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:detail' % self._meta.app_label, args=(self.pk,))

    def get_create_url(self):
        try:
            return reverse('%s:create' % self._meta.model_name)
        except:
            return reverse('%s:create' % self._meta.app_label)

    def get_read_url(self):
        try:
            return reverse('%s:read' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:read' % self._meta.app_label, args=(self.pk,))

    def get_update_url(self):
        try:
            return reverse('%s:update' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:update' % self._meta.app_label, args=(self.pk,))

    def get_delete_url(self):
        try:
            return reverse('%s:delete' % self._meta.model_name, args=(self.pk,))
        except:
            return reverse('%s:delete' % self._meta.app_label, args=(self.pk,))

    def get_verbose_name(self):
        # if isinstance(self, QuerySet):
        #     return self._meta.verbose_name
        # else:
        #     return self.verbose_name
        return self._meta.verbose_name

    def get_verbose_name_plural(self):
        return self._meta.verbose_name_plural

    def delete(self):
        self.deleted = True
        self.save()

    def hard_delete(self, *args, **kwargs):
        super(Auditable, self).delete(*args,**kwargs)        


class Universidad(Auditable):
    nombre = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'ceu_universidades'
        verbose_name = 'Universidad'
        verbose_name_plural = 'Universidades'

    def __str__(self):
        return self.nombre
    

class Campus(Auditable):
    universidad = models.ForeignKey(Universidad, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'ceu_campus'
        verbose_name = 'Campus'
        verbose_name_plural = 'Cumpus'

    def __str__(self):
        return self.nombre


class Area(Auditable):
    nombre = models.CharField(max_length=50)
    icono = models.CharField(max_length=25, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_areas'
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.nombre


class TipoTitulacion(Auditable):
    nombre = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_tipos_titulaciones'
        verbose_name = 'Tipo de Titulación'
        verbose_name_plural = 'Tipos de Titulaciones'

    def __str__(self):
        return self.nombre


class Titulacion(Auditable):
    TIPO = ( ('A', 'año'), ('M', 'mes'), ('D', 'día'), ('H', 'hora') )
    MODALIDAD = ( ('P', 'Presencial'), ('S', 'Semipresencial'), ('O', 'Online') )
    
    campus = models.ManyToManyField(Campus, through='CampusTitulacion')
    area = models.ManyToManyField(Area, through='AreaTitulacion',)
    tipo_titulacion = models.ForeignKey(TipoTitulacion, models.DO_NOTHING, blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True, help_text='cantidad de (año/mes/dia/hora)')
    duracion_tipo = models.CharField(max_length=1, blank=True, null=True, choices=TIPO)
    nombre = models.CharField(max_length=160, help_text='solo para referencia, utilizar asignatura_idiomas.nombre')
    creditos = models.SmallIntegerField(blank=True, null=True, help_text='sumatoria de créditos de todas las materias')
    modalidad = models.CharField(max_length=1, blank=True, null=True, choices=MODALIDAD)
    insercion_laboral = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True, help_text='tasa de inserción laboral según ranking BBVA e IVIE')
    citrix = models.CharField(max_length=5, blank=True, null=True, help_text='código referencia CITRIX', verbose_name='Cód. CITRIX', unique=True)
    sigma = models.BigIntegerField(blank=True, null=True, help_text='código referencia SIGMA', verbose_name='Cód. SIGMA', unique=True)


    class Meta:
        # managed = False
        db_table = 'ceu_titulaciones'
        verbose_name = 'Titulación'
        verbose_name_plural = 'Titulaciones'

    def __str__(self):
        return self.nombre


class TitulacionIdioma(Auditable):
    IDIOMA = ( ('es', 'Español'), ('en', 'Inglés'), ('fr', 'Francés') )
    
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=160)
    idioma = models.CharField(max_length=2, default='es', choices=IDIOMA, blank=True, null=True, help_text='idioma en el que se impartirá la asignatura (es, en, fr)')

    class Meta:
        db_table = 'ceu_titulacion_idiomas'
        verbose_name = 'Titulación Idioma'
        verbose_name_plural = 'Titulación Idiomas'
        unique_together = ['titulacion', 'idioma']

    def __str__(self):
        return self.nombre


class PlanEstudio(Auditable):
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    ciclo_lectivo = models.IntegerField(blank=True, null=True, help_text='año correspondiente al plan de estudio')

    class Meta:
        # managed = False
        db_table = 'ceu_planes_estudios'
        verbose_name = 'Plan de Estudio'
        verbose_name_plural = 'Planes de Estudios'
        unique_together = ['titulacion', 'ciclo_lectivo']

    def __str__(self):
        return '{} - {}'.format(self.ciclo_lectivo, self.titulacion.nombre)


class Curso(Auditable):
    plan_estudio = models.ForeignKey(PlanEstudio, models.DO_NOTHING, blank=True, null=True)
    curso = models.SmallIntegerField()
    nombre = models.CharField(max_length=50)

    class Meta:
        # managed = False
        db_table = 'ceu_cursos'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        unique_together = ['plan_estudio', 'curso']

    def __str__(self):
        return '{} {} - {}'.format(self.plan_estudio.ciclo_lectivo, self.plan_estudio.titulacion, self.nombre)


class Asignatura(Auditable):
    curso = models.ManyToManyField(Curso, through='CursoAsignatura')
    nombre = models.CharField(max_length=160, help_text='solo para referencia, utilizar asignatura_idiomas.nombre')
    creditos = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    citrix = models.CharField(max_length=5, blank=True, null=True, help_text='código referencia CITRIX', verbose_name='Cód. CITRIX', unique=True)
    sigma = models.BigIntegerField(blank=True, null=True, help_text='código referencia SIGMA', verbose_name='Cód. SIGMA', unique=True)

    class Meta:
        # managed = False
        db_table = 'ceu_asignaturas'
        verbose_name = 'Asignatura'
        verbose_name_plural = 'Asignaturas'

    def __str__(self):
        return self.nombre


class AsignaturaIdioma(Auditable):
    asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, blank=True, null=True)
    nombre = models.CharField(max_length=160)
    idioma = models.CharField(max_length=2, blank=True, null=True, help_text='idioma en el que se impartirá la asignatura (es, en, fr)')

    class Meta:
        # managed = False
        db_table = 'ceu_asignatura_idiomas'
        verbose_name = 'Asignatura Idioma'
        verbose_name_plural = 'Asignatura Idiomas'
        unique_together = ['asignatura', 'idioma']

    def __str__(self):
        # return '{} / {}'.format(self.asignatura.id, self.idioma)
        return '{}'.format(self.id)
    

class Persona(Auditable):
    SEXO = ( ('H', 'Hombre'), ('M', 'Mujer') )

    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    dni = models.CharField(max_length=9, blank=True, null=True, unique=True)
    sexo = models.CharField(max_length=1, default='H', choices=SEXO, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_personas'
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return '{}, {}'.format(self.apellidos, self.nombre)

    @property
    def nombre_apellidos(self):
        return '{} {}'.format(self.persona.nombre, self.persona.apellidos)

    @property
    def apellidos_nombre(self):
        return '{}, {}'.format(self.persona.apellidos, self.persona.nombre)
    

class Profesor(Auditable):
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
    def nombre_apellidos(self):
        return '{} {}'.format(self.persona.nombre, self.persona.apellidos)

    @property
    def apellidos_nombre(self):
        return '{}, {}'.format(self.persona.apellidos, self.persona.nombre)
    
    @property
    def foto_preview(self):
        if self.foto:
            return mark_safe('<img src="{}" width="200" height="200" style="border-radius: 10%"/>'.format(self.foto.url))
        return ''
    

class Funcion(Auditable):
    profesor = models.ManyToManyField(Profesor, through='ProfesorFuncion')
    nombre = models.CharField(max_length=150)

    class Meta:
        # managed = False
        db_table = 'ceu_funciones'
        verbose_name = 'Función'
        verbose_name_plural = 'Funciones'

    def __str__(self):
        return self.nombre
    

# -----------------------------------------------------------------------------
# relaciones ManyToMany
# -----------------------------------------------------------------------------


class CampusTitulacion(Auditable):
    id = models.BigAutoField(primary_key=True)
    campus = models.ForeignKey(Campus, models.DO_NOTHING, related_name='campus_titulacion')
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, related_name='titulacion_campus')
    guid = models.CharField(max_length=36, blank=True, null=True)
    plazas = models.SmallIntegerField(blank=True, null=True)
    url_calendario = models.CharField(max_length=160, blank=True, null=True, verbose_name='URL Calendario')
    url_horario = models.CharField(max_length=160, blank=True, null=True, verbose_name='URL Horario')

    class Meta:
        # managed = False
        db_table = 'ceu_campus_titulaciones'
        verbose_name = 'Cumpus Titulación'
        verbose_name_plural = 'Cumpus Titulaciones'
        unique_together = ['campus', 'titulacion']

    def __str__(self):
        return 'id: {} / Campus: {} / Titulación: {}'.format(self.id, self.campus.id, self.titulacion.id)


class AreaTitulacion(Auditable):
    id = models.BigAutoField(primary_key=True)
    area = models.ForeignKey(Area, models.DO_NOTHING, related_name='area_titulacion', limit_choices_to={'parent_id__isnull': False})
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, related_name='titulacion_area')

    class Meta:
        # managed = False
        db_table = 'ceu_areas_titulaciones'
        verbose_name = 'Area Titulación'
        verbose_name_plural = 'Areas Titulaciones'
        unique_together = ['area', 'titulacion']

    def __str__(self):
        return 'id: {} / Area: {} / Titulación: {}'.format(self.id, self.area.id, self.titulacion.id)


class CursoAsignatura(Auditable):
    PERIODO = ( ('T', 'Trimestre'), ('C', 'Cuatrimestre'), ('S', 'Semestre') )
    TIPO = ( ('FB', 'Formación básica'), ('OB', 'Obligatoria'), ('OP', 'Optativa'), ('PR', 'Práctica'), ('TFG', 'Trabajo fin de grado') )
    
    id = models.BigAutoField(primary_key=True)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, related_name='curso_asignatura')
    asignatura = models.ForeignKey(Asignatura, models.DO_NOTHING, related_name='asignatura_curso')
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING, blank=True, null=True)
    periodo = models.CharField(max_length=2, blank=True, null=True, choices=PERIODO)
    creditos = models.DecimalField(max_digits=5, decimal_places=1, blank=True, null=True)
    tipo = models.CharField(max_length=3, blank=True, null=True, choices=TIPO)
    url_guia = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ceu_cursos_asignaturas'
        verbose_name = 'Curso Asignatura'
        verbose_name_plural = 'Cursos Asignaturas'
        unique_together = ['curso', 'asignatura']

    def __str__(self):
        return 'id: {} / Curso: {} / Asignatura: {}'.format(self.id, self.curso.id, self.asignatura.id)


class ProfesorFuncion(Auditable):
    id = models.BigAutoField(primary_key=True)
    profesor = models.ForeignKey(Profesor, models.DO_NOTHING, related_name='profesor_funcion')
    funcion = models.ForeignKey(Funcion, models.DO_NOTHING, related_name='funcion_profesor')
    prioridad = models.SmallIntegerField(blank=True, null=True)
    PRINCIPAL = ( (True, 'Sí'), (False, 'No') )
    principal = models.BooleanField(default=False, choices=PRINCIPAL, blank=True, null=True, help_text='función o cargo principal')

    class Meta:
        # managed = False
        db_table = 'ceu_profesores_funciones'
        verbose_name = 'Profesor Función'
        verbose_name_plural = 'Profesores Funciones'
        unique_together = ['profesor', 'funcion']
    
    def __str__(self):
        return 'id: {} / Profesor: {} / Función: {}'.format(self.id, self.profesor.id, self.funcion.id)


# -----------------------------------------------------------------------------
# tablas relacionadas con las tablas ManyToMany
# -----------------------------------------------------------------------------

class JPA(Auditable):
    TIPO = ( ('O', 'Online'), ('P', 'Presencial'), ('S', 'Semipresencial') )

    campus_titulacion = models.ForeignKey(CampusTitulacion, models.DO_NOTHING, blank=True, null=True)
    fecha = models.DateField()
    tipo = models.CharField(max_length=1, default='P', choices=TIPO, blank=True, null=True, help_text='Online, Presencial, Semipresencial)')
    es_nacional = models.BooleanField('¿Nacional?', default=True)

    class Meta:
        db_table = 'ceu_jpa'
        verbose_name = 'Jornada a Puerta Abierta'
        verbose_name_plural = 'Jornadas de Puertas Abiertas'

    def __str__(self):
        return self.id


class JPAIdiomas(Auditable):
    IDIOMA = ( ('es', 'Español'), ('en', 'Inglés'), ('fr', 'Francés') )
    
    jpa = models.ForeignKey(JPA, models.DO_NOTHING, blank=True, null=True)
    idioma = models.CharField(max_length=2, default='es', choices=IDIOMA, blank=True, null=True, help_text='idioma en el que se impartirá la asignatura (es, en, fr)')

    class Meta:
        db_table = 'ceu_jpa_idiomas'
        verbose_name = 'JPA Idioma'
        verbose_name_plural = 'JPA Idiomas'
        unique_together = ['jpa', 'idioma']

    def __str__(self):
        return self.id



# -----------------------------------------------------------------------------
# vistas
# -----------------------------------------------------------------------------


class TitulacionesView(models.Model): 
    id = models.BigIntegerField(primary_key=True)   # campo unico para la vista   ceu_areas_titulaciones.['area', 'titulacion']
    
    campus_id = models.BigIntegerField()
    campus = models.CharField(max_length=50)

    area_id = models.BigIntegerField()
    area = models.CharField(max_length=50)
    subarea_id = models.BigIntegerField()
    subarea = models.CharField(max_length=50)
    
    tipo_titulacion_id = models.BigIntegerField()
    tipo_titulacion = models.CharField(max_length=50)

    titulacion_id = models.BigIntegerField()
    titulacion = models.CharField(max_length=160)
    sigma = models.BigIntegerField()
    citrix = models.CharField(max_length=5)

    duracion = models.IntegerField()
    TIPO = ( ('A', 'año'), ('M', 'mes'), ('D', 'día'), ('H', 'hora') )
    duracion_tipo = models.CharField(max_length=1, blank=True, null=True, choices=TIPO)
    creditos = models.SmallIntegerField()
    
    class Meta:
        managed = False
        db_table = 'ceu_titulaciones_view'





# -----------------------------------------------------------------------------
# pruebas, posiblemente no serán necesarias
# -----------------------------------------------------------------------------


class TitulacionAux(Auditable):
    TIPO = ( ('F', 'Fijo'), ('M', 'Móvil') )
    
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    tipo_encabezado = models.CharField(max_length=1, choices=TIPO, default='F')
    
    url_imagen_1 = models.CharField(max_length=160)
    text_imagen_1 = models.CharField(max_length=160)
    subtext_imagen_1 = models.CharField(max_length=160)

    url_imagen_2 = models.CharField(max_length=160, blank=True, null=True)
    text_imagen_2 = models.CharField(max_length=160, blank=True, null=True)
    subtext_imagen_2 = models.CharField(max_length=160, blank=True, null=True)

    url_imagen_3 = models.CharField(max_length=160, blank=True, null=True)
    text_imagen_3 = models.CharField(max_length=160, blank=True, null=True)
    subtext_imagen_3 = models.CharField(max_length=160, blank=True, null=True)

    class Meta:
        db_table = 'ceu_titulacion_aux'
        verbose_name = 'Titulación AUX'
        verbose_name_plural = 'Titulaciones AUX'


class TitulacionHTML(Auditable):
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    grupo = models.CharField(max_length=80, blank=True, null=True)
    titulo = models.CharField(max_length=80, blank=True, null=True) 
    texto = RichTextField(blank=True, null=True)

    class Meta:
        db_table = 'ceu_titulacion_html'
        verbose_name = 'Titulación HTML'
        verbose_name_plural = 'Titulaciones HTML'


class TitulacionURL(Auditable):
    titulacion = models.ForeignKey(Titulacion, models.DO_NOTHING, blank=True, null=True)
    grupo = models.CharField(max_length=80, blank=True, null=True)
    url = models.CharField(max_length=180, blank=True, null=True) 
    texto = models.CharField(max_length=80, blank=True, null=True) 

    class Meta:
        db_table = 'ceu_titulacion_url'
        verbose_name = 'Titulación URL'
        verbose_name_plural = 'Titulaciones URL'
