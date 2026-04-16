from django.contrib import admin

from .models import Asistencia


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_completo",
        "documento_identidad",
        "fecha_asistencia",
        "hora_ingreso",
        "hora_salida",
        "presente",
    )
    search_fields = ("nombre_completo", "documento_identidad", "correo_electronico")
    list_filter = ("presente", "fecha_asistencia")

# Register your models here.
