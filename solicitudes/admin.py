from django.contrib import admin

from .models import Solicitud


@admin.register(Solicitud)
class SolicitudAdmin(admin.ModelAdmin):
    list_display = (
        "nombre_solicitante",
        "documento_identidad",
        "tipo_solicitud",
        "fecha_solicitud",
        "correo_electronico",
    )
    search_fields = ("nombre_solicitante", "documento_identidad", "correo_electronico")
    list_filter = ("tipo_solicitud", "fecha_solicitud")

# Register your models here.
