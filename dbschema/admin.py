from django.contrib import admin

# from django.forms import TextInput
# from django.db import models


from .models import \
    Area, Asignatura, AsignaturaIdioma, \
    Campus, CampusTitulacion, Competencia, Curso, CursoAsignatura, \
    Funcion, \
    PlanEstudio, Persona, Profesor, \
    SalidaProfesional, \
    TipoTitulacion, Titulacion, TitulacionIdioma, \
    Universidad


@admin.register(Universidad)
class UniversidadAdmin(admin.ModelAdmin):
    pass


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    pass


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    ordering = ['nombre']


@admin.register(TipoTitulacion)
class TipoTitulacionAdmin(admin.ModelAdmin):
    pass


class TitulacionIdiomaInLine(admin.StackedInline):
    # TabularInline):
    # list_display = ['id', 'departamento', 'nombre', 'cod_postal', 'cod_area_tel', 'active']
    # list_display_links = ['nombre']
    # list_filter = ['departamento__nombre']
    # search_fields = ['nombre']
    # ordering = ['nombre']
    model = TitulacionIdioma
    fields = ['nombre', 'idioma']
    # readonly_fields = fields
    ordering = ['nombre']
    extra = 0
    can_delete = False
    # show_change_link = True    
    view_on_site = False

class CompetenciaInLine(admin.TabularInline):
    model = Competencia
    fields = ['grupo', 'texto']
    ordering = ['grupo']
    extra = 0
    can_delete = False
    view_on_site = False

class SalidaProfesionalInLine(admin.TabularInline):
    model = SalidaProfesional
    fields = ['grupo', 'texto']
    ordering = ['grupo']
    extra = 0
    can_delete = False
    view_on_site = False

class PlanEstudioProfesionalInLine(admin.TabularInline):
    model = PlanEstudio
    fields = ['ciclo_lectivo']
    ordering = ['ciclo_lectivo']
    extra = 0
    can_delete = False
    view_on_site = True

@admin.register(Titulacion)
class TitulacionAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    list_display_links = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    inlines = [TitulacionIdiomaInLine, CompetenciaInLine, SalidaProfesionalInLine, PlanEstudioProfesionalInLine]


@admin.register(PlanEstudio)
class PlanEstudioAdmin(admin.ModelAdmin):
    view_on_site = True
    pass


class AsignaturaIdiomaInLine(admin.StackedInline):
    model = AsignaturaIdioma
    fields = ['nombre', 'idioma']
    # readonly_fields = fields
    ordering = ['nombre']
    extra = 0
    can_delete = False
    # show_change_link = True    
    view_on_site = False

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'codigo', 'creditos']
    list_display_links = ['nombre']
    search_fields = ['nombre', 'codigo']
    ordering = ['nombre']
    inlines = [AsignaturaIdiomaInLine]


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    def apellidos_nombre(self, obj):
        return '{0}, {1}'.format(obj.apellidos, obj.nombre)
    
    list_display = ['id', 'apellidos_nombre']
    list_display_links = ['apellidos_nombre']
    search_fields = ['nombre', 'apellidos']
    ordering = ['apellidos', 'nombre']

    def get_form(self, request, obj=None, **kwargs):
        form = super(PersonaAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['apellidos'].widget.attrs['style'] = 'width: 35em;'
        return form


class FuncionInLine(admin.StackedInline):
    model = Funcion
    fields = ['nombre', 'principal']
    ordering = ['nombre']
    extra = 0
    can_delete = False
    view_on_site = False

    def get_formset(self, request, obj=None, **kwargs):
        form = super(FuncionInLine, self).get_formset(request, obj, **kwargs)
        form.form.base_fields['nombre'].widget.attrs['style'] = 'width: 45em;'
        return form


@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    def nombre_apellidos(self, obj):
        return '{0} {1}'.format(obj.persona.nombre, obj.persona.apellidos)

    def foto_preview(self, obj):
        return obj.foto_preview
    foto_preview.short_description = 'Vista previa'
    foto_preview.allow_tags = True

    nombre_apellidos.short_description = 'Nombre'
    readonly_fields = ('foto_preview',)

    list_display = ['id', 'nombre_apellidos']
    list_display_links = ['nombre_apellidos']
    ordering = ['persona__nombre', 'persona__apellidos']
    inlines = [FuncionInLine]

    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if not isinstance(inline, FuncionInLine) or obj is not None:
                yield inline.get_formset(request, obj), inline
