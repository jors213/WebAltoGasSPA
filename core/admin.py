from django.contrib import admin
from .models import Contacto, SolicitudAsesoria

# Configuración visual para el Panel de Administración
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'fecha_creacion') # Qué columnas ver
    search_fields = ('nombre', 'telefono', 'email') # Barra de búsqueda
    list_filter = ('fecha_creacion',) # Filtro lateral por fecha
    readonly_fields = ('fecha_creacion',) # Para que nadie pueda falsificar la fecha

admin.site.register(Contacto, ContactoAdmin)


@admin.register(SolicitudAsesoria)
class SolicitudAsesoriaAdmin(admin.ModelAdmin):
    list_display  = ('nombre', 'telefono', 'email', 'tipo_asesoria', 'fecha_creacion')
    list_filter   = ('tipo_asesoria', 'fecha_creacion')
    search_fields = ('nombre', 'telefono', 'email')
    readonly_fields = ('fecha_creacion',)