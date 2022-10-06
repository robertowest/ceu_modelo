from dataclasses import fields
import string
from django.contrib import admin

# from django.forms import TextInput
# from django.db import models


from .models import \
    Area, Asignatura, AsignaturaIdioma, \
    Campus, CampusTitulacion, Curso, CursoAsignatura, \
    Funcion, \
    PlanEstudio, Persona, Profesor, ProfesorFuncion, \
    TipoTitulacion, Titulacion, TitulacionHTML, TitulacionIdioma, TitulacionURL, \
    Universidad


# ordenamos la lista de aplicaciones según el orden definido de los modelos
from config.admin import my_get_app_list
admin.AdminSite.get_app_list = my_get_app_list


class MyModelAdmin(admin.ModelAdmin):
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({'show_delete': False})
        return super().render_change_form(request, context, add, change, form_url, obj)    


class FirstLetterListFilter(admin.SimpleListFilter):
    """
    Filtro definido por la primera letra del campo 'nombre' de la tabla
    """
    title = 'Índice'

    # parámetro para el filtro que se utilizará en la URL
    parameter_name = 'letra'
    letters = list(string.ascii_uppercase)

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        lookups = []
        for letter in self.letters:
            count = qs.filter(nombre__istartswith=letter).count()
            if count:
                lookups.append((letter, '{} ({})'.format(letter, count)))
        return lookups

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        filter_val = self.value()
        if filter_val in self.letters:
            return queryset.filter(nombre__istartswith=self.value())
    

# ---------------------------------------------------------------------------------------

class CampusInLine(admin.TabularInline):
    model = Campus
    readonly_fields = ['nombre', 'is_deleted']
    ordering = ['nombre']
    extra = 0
    can_delete = False
    view_on_site = False
    show_change_link = True

@admin.register(Universidad)
class UniversidadAdmin(MyModelAdmin):
    fields = ['nombre', 'is_deleted']
    inlines = [CampusInLine]

# ---------------------------------------------------------------------------------------

@admin.register(Campus)
class CampusAdmin(MyModelAdmin):
    fields = ['universidad', 'nombre', 'is_deleted']

# ---------------------------------------------------------------------------------------

class ParentIdListFilter(admin.SimpleListFilter):
    # https://docs.djangoproject.com/en/4.1/ref/contrib/admin/filters/
    title = 'Area principal'
    parameter_name = 'id'

    def lookups(self, request, model_admin):
        return Area.objects.filter(parent__isnull=True).values_list('id', 'nombre').order_by('nombre')

    def queryset(self, request, queryset):
        return queryset.filter(parent=self.value())

@admin.register(Area)
class AreaAdmin(MyModelAdmin):
    fields = ['parent', 'nombre', 'icono', 'is_deleted']
    list_display = ['id', 'nombre', 'icono', 'is_deleted']
    list_display_links = ['nombre']
    list_filter = [ParentIdListFilter]
    ordering = ['nombre']

# ---------------------------------------------------------------------------------------

@admin.register(TipoTitulacion)
class TipoTitulacionAdmin(MyModelAdmin):
    fields = ['nombre', 'is_deleted']

# ---------------------------------------------------------------------------------------

@admin.register(TitulacionIdioma)
class TitulacionIdiomaAdmin(MyModelAdmin):
    fields = ['titulacion', 'idioma', 'nombre', 'is_deleted']
    
# ---------------------------------------------------------------------------------------

class CampusTitulacionInLine(admin.StackedInline):
    model = Titulacion.campus.through
    verbose_name_plural = 'Campus donde se imparte la titulación'
    fields = ['campus', 'citrix', 'guid', 'plazas', 'url_calendario', 'url_horario', 'is_deleted']
    extra = 0
    can_delete = False
    show_change_link = False
    view_on_site = False

class AreaTitulacionInLine(admin.TabularInline):
    model = Titulacion.area.through
    # fields = ['nombre', 'idioma']
    # readonly_fields = fields
    # ordering = ['nombre']
    extra = 0
    can_delete = False
    # show_change_link = True    
    view_on_site = False

class TitulacionIdiomaInLine(admin.TabularInline):
    model = TitulacionIdioma
    fields = ['nombre', 'idioma', 'is_deleted']
    ordering = ['nombre']
    extra = 0   # max_num = 0
    can_delete = False
    show_change_link = True    
    view_on_site = False

class PlanEstudioProfesionalInLine(admin.TabularInline):
    model = PlanEstudio
    fields = ['ciclo_lectivo', 'is_deleted']
    ordering = ['ciclo_lectivo']
    extra = 0   # max_num = 0
    can_delete = False
    view_on_site = True

# class TitulacionHTMLInLine(admin.StackedInline):
#     verbose_name_plural = 'Campos HTML relacionados'
#     model = TitulacionHTML
#     fields = ['grupo', 'titulo', 'texto', 'is_deleted']
#     ordering = ['grupo', 'id']
#     extra = 0   # max_num = 0
#     can_delete = False
#     view_on_site = False

# class TitulacionURLInLine(admin.TabularInline):
#     verbose_name_plural = 'URL relacionados'
#     model = TitulacionURL
#     fields = ['grupo', 'url', 'texto', 'is_deleted']
#     ordering = ['grupo', 'id']
#     extra = 0   # max_num = 0
#     can_delete = False
#     view_on_site = False

@admin.register(Titulacion)
class TitulacionAdmin(MyModelAdmin):
    fields = ['tipo_titulacion', 'nombre', 'sigma', 'duracion', 'duracion_tipo', 'creditos', 'modalidad', 'insercion_laboral', 'is_deleted']
    list_display = ['id', 'nombre', 'sigma']
    list_display_links = ['nombre']
    search_fields = ['nombre', 'sigma']
    ordering = ['nombre']
    inlines = [CampusTitulacionInLine, AreaTitulacionInLine, TitulacionIdiomaInLine, PlanEstudioProfesionalInLine]
    # TitulacionHTMLInLine, TitulacionURLInLine

# ---------------------------------------------------------------------------------------

from dbschema.models import TitulacionAux

@admin.register(TitulacionAux)
class TitulacionAuxAdmin(MyModelAdmin):
    fieldsets = (
        (None, {
           'fields': ('titulacion', 'tipo_encabezado', 'url_imagen_1', 'text_imagen_1', 'subtext_imagen_1')
        }),
        ('Campos para diapositivas', {
            'fields': ('url_imagen_2', 'text_imagen_2', 'subtext_imagen_2', 
                       'url_imagen_3', 'text_imagen_3', 'subtext_imagen_3'),
            'classes': ('collapse', ),
        }),
    )    
    
    class Media:
        js = ['js/my_code.js']

# ---------------------------------------------------------------------------------------

@admin.register(CampusTitulacion)
class CampusTitulacionAdmin(MyModelAdmin):
    fields = ['titulacion', 'guid', 'plazas', 'url_calendario', 'url_horario', 'is_deleted']
    list_display = ['titulacion', 'is_deleted']
    # list_display_links = ['citrix']
    list_filter = ['campus']
    # search_fields = ['citrix']
    # ordering = ['citrix']

# ---------------------------------------------------------------------------------------

class CursoInLine(admin.TabularInline):
    model = Curso
    fields = ['nombre']
    ordering = ['nombre']
    extra = 0
    can_delete = False
    view_on_site = True

@admin.register(PlanEstudio)
class PlanEstudioAdmin(MyModelAdmin):
    fields = ['titulacion', 'ciclo_lectivo', 'is_deleted']
    inlines = [CursoInLine]

# ---------------------------------------------------------------------------------------

# # class CursoAsignaturaInLine(admin.TabularInline):
# #     model = CursoAsignatura
# #     fields = ['id', 'curso', 'asignatura', 'profesor', 'periodo', 'creditos', 'tipo']
# #     # ordering = ['nombre']
# #     extra = 0
# #     can_delete = False
# #     view_on_site = True

@admin.register(Curso)
class CursoAdmin(MyModelAdmin):
    # inlines = [CursoAsignaturaInLine]
    # list_display = ['id', 'nombre', 'get_asignatura']
    fields = ['plan_estudio', 'nombre', 'is_deleted']
    list_display = ['id', 'plan_estudio', 'nombre', 'is_deleted']
    list_display_links = ['nombre']
    ordering = ['nombre']

# def get_asignatura(self, obj):
#     # return [asignatura.nombre for asignatura in obj.asignatura.all()]
#     return "hola"

# ---------------------------------------------------------------------------------------

class AsignaturaIdiomaInLine(admin.StackedInline):
    model = AsignaturaIdioma
    fields = ['nombre', 'idioma', 'is_deleted']
    readonly_fields = fields
    ordering = ['nombre']
    extra = 0
    can_delete = False
    show_change_link = True
    view_on_site = False

@admin.register(Asignatura)
class AsignaturaAdmin(MyModelAdmin):
    fields = ['nombre', 'sigma', 'creditos', 'is_deleted']
    list_display = ['id', 'nombre', 'sigma', 'creditos']
    list_display_links = ['nombre']
    search_fields = ['nombre', 'sigma']
    ordering = ['nombre']
    inlines = [AsignaturaIdiomaInLine]

# ---------------------------------------------------------------------------------------

class ProfesorInLine(admin.TabularInline):
    def nombre_apellidos(self, obj):
        return '{0} {1}'.format(obj.persona.nombre, obj.persona.apellidos)

    model = Profesor
    verbose_name = "Profesor"
    verbose_name_plural = "Ficha de Profesor"

    fields = ['id', 'persona', 'foto', 'is_deleted']
    readonly_fields = fields
    extra = 0
    can_delete = False
    view_on_site = False
    show_change_link = True
    
@admin.register(Persona)
class PersonaAdmin(MyModelAdmin):
    def apellidos_nombre(self, obj):
        return '{0}, {1}'.format(obj.apellidos, obj.nombre)
    
    fields = ['nombre', 'apellidos', 'dni', 'sexo', 'is_deleted']
    list_display = ['id', 'apellidos_nombre']
    list_display_links = ['apellidos_nombre']
    search_fields = ['nombre', 'apellidos']
    ordering = ['apellidos', 'nombre']
    inlines = [ProfesorInLine]

    def get_form(self, request, obj=None, **kwargs):
        form = super(PersonaAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['apellidos'].widget.attrs['style'] = 'width: 35em;'
        return form

# ---------------------------------------------------------------------------------------

class FuncionesInLine(admin.TabularInline):
    verbose_name_plural = 'Funciones asociadas'
    model = ProfesorFuncion
    fields = ['id', 'funcion', 'prioridad', 'principal', 'is_deleted']
    readonly_fields = fields
    ordering = ['prioridad']
    extra = 0
    can_delete = False
    show_change_link = True
    view_on_site = False

@admin.register(Profesor)
class ProfesorAdmin(MyModelAdmin):
    def nombre_apellidos(self, obj):
        return '{0} {1}'.format(obj.persona.nombre, obj.persona.apellidos)

    def foto_preview(self, obj):
        return obj.foto_preview
    foto_preview.short_description = 'Vista previa'
    foto_preview.allow_tags = True

    nombre_apellidos.short_description = 'Nombre'
    readonly_fields = ('foto_preview',)

    fields = ['persona', 'foto', readonly_fields, 'is_deleted']
    list_display = ['id', 'nombre_apellidos']
    list_display_links = ['nombre_apellidos']
    search_fields = ['persona__nombre', 'persona__apellidos']
    ordering = ['persona__nombre', 'persona__apellidos']
    inlines = [FuncionesInLine]

# ---------------------------------------------------------------------------------------

class ProfesorInLine(admin.TabularInline):
    model = Funcion.profesor.through
    verbose_name_plural = 'Profesores con esta función'
    fields = ['profesor', 'prioridad', 'principal', 'is_deleted']
    readonly_fields = fields
    extra = 0
    can_delete = False
    view_on_site = False
    show_change_link = True
    
@admin.register(Funcion)
class FuncionAdmin(MyModelAdmin):
    fields = ['nombre', 'is_deleted']
    list_display = ['id', 'nombre']
    list_display_links = ['nombre']
    list_filter = [FirstLetterListFilter]
    search_fields = ['nombre']
    ordering = ['nombre']
    inlines = [ProfesorInLine]

# ---------------------------------------------------------------------------------------


# # modelo de una vista representado en site admin
# from .models import TitulacionesView
# @admin.register(TitulacionesView)
# class TitulacionesViewAdmin(MyModelAdmin):
#     list_display = ['id', 'titulacion']
