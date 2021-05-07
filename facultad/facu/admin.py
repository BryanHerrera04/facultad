from django.contrib import admin
from facu.models import Decano, Facultad, Docente, Asignatura, Estudiante
from import_export.admin import ImportExportModelAdmin

# Register your models here.


class DecanoAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nom_decano', 'ape_decano', 'cedula', 'cel_decano',)
    search_fields = ('nom_decano',)
    # list_filter=('column',)


class FacultadAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nom_facultad', 'num_blo_facultad',
                    'ubi_facultad', 'decano',)
    search_fields = ('nom_facultad',)
    # list_filter=('column',)


class DocenteAsignatura(admin.TabularInline):
    model = Asignatura
    can_delete = True
    extra = 0


class DocenteAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nom_docente', 'ape_docente',
                    'cc_docente', 'titulo_docente', 'facultad')
    search_fields = ('nom_decano',)
    # list_filter=('column',)

    inlines = [DocenteAsignatura]


class AsignaturaEstudiante(admin.TabularInline):
    model = Estudiante
    can_delete = True
    extra = 0


class AsignaturaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nom_asig', 'cod_asig', 'num_cred_asig', 'docente', )
    search_fields = ('nom_facultad',)
    # list_filter=('column',)

    inlines = [AsignaturaEstudiante]


class EstudianteAdmin(ImportExportModelAdmin):
    list_display = ('id', 'nom_est', 'ape_est',
                    'cc_est', 'dir_est', 'asignatura')
    search_fields = ('nom_facultad',)
    # list_filter=('column',)


admin.site.register(Decano, DecanoAdmin)
admin.site.register(Facultad, FacultadAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Asignatura, AsignaturaAdmin)
admin.site.register(Estudiante, EstudianteAdmin)
