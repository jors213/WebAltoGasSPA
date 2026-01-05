from django.contrib import admin
from .models import Contacto

# Configuración visual para el Panel de Administración
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'email', 'fecha_creacion') # Qué columnas ver
    search_fields = ('nombre', 'telefono', 'email') # Barra de búsqueda
    list_filter = ('fecha_creacion',) # Filtro lateral por fecha
    readonly_fields = ('fecha_creacion',) # Para que nadie pueda falsificar la fecha

admin.site.register(Contacto, ContactoAdmin)