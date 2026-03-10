from django.contrib import admin
from .models import Estudiante, Expediente1, Expediente2, Resolucion

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['apellidos_nombres', 'dni', 'escuela', 'fecha_creacion']
    search_fields = ['apellidos_nombres', 'dni']

admin.site.register(Expediente1)
admin.site.register(Expediente2)
admin.site.register(Resolucion)
