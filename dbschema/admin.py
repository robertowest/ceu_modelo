import string

from dataclasses import fields
from django.contrib import admin

from .models import \
    Area, Asignatura, AsignaturaIdioma, \
    Campus, CampusTitulacion, Curso, CursoAsignatura, \
    Departamento, \
    Facultad, Funcion, \
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

@admin.register(Facultad)
class FacultadAdmin(MyModelAdmin):
    fields = ['nombre', 'is_deleted']

# ---------------------------------------------------------------------------------------

@admin.register(Departamento)
class DepartamentoAdmin(MyModelAdmin):
    list_display = ['nombre', 'is_deleted']
    list_filter = ['facultad']

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
    # fields = ['parent', 'nombre', 'icono', 'is_deleted']
    list_display = ['id', 'nombre', 'icono', 'is_deleted']
    list_display_links = ['nombre']
    list_filter = [ParentIdListFilter]
    ordering = ['nombre']

# ---------------------------------------------------------------------------------------
