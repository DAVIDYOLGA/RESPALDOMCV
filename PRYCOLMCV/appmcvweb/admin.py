from django.contrib import admin
from .models import grupo
from .models import inicio
from .models import publicacion
from .models import actividad
from .models import presentacion
from .models import comunicado
from .models import aplicacion

admin.site.site_header = "COLEGIO MANUEL CEPEDA VARGAS"
admin.site.index_title = "ACTUALIZACION DE LA PAGINA WEB"
admin.site.site_title = "COL MCV IED"

# Register your models here.

@admin.register(grupo)
class grupoadmin(admin.ModelAdmin):
    list_display = ('nombre', 'updated' )
    list_per_page = 12

@admin.register(inicio)
class inicioadmin(admin.ModelAdmin):
    list_display = ('titulo', 'grupo', 'enlace', 'updated')
    ordering = ['updated']
    search_fields = ['titulo']
    list_editable = ['grupo']
    list_filter =  ['grupo']
    list_per_page = 12

@admin.register(presentacion)
class presentacionadmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'updated' )
    list_per_page = 12

@admin.register(publicacion)
class publicacionadmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'grupo', 'imagen', 'updated' )
    list_per_page = 12

@admin.register(actividad)
class actividadadmin(admin.ModelAdmin):
    list_display = ('titulo', 'grupo', 'fechaact', 'imagen', 'updated' )
    ordering = ('-fechaact','titulo',)
    #search_fields = ('titulo', 'grupo')
    list_filter = ('titulo',)
    list_per_page = 12
    #exclude = ('titulo',)   para no permitir que se pueda modificar un campo

@admin.register(comunicado)
class comunicadoadmin(admin.ModelAdmin):
    list_display = ('titulo', 'grupo', 'fechaact' )
    list_per_page = 12 

@admin.register(aplicacion)
class aplicacionadmin(admin.ModelAdmin):
    list_display = ('titulo', 'imagen', 'updated')
    list_per_page = 12