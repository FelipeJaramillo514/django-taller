from datetime import date

from django.core.exceptions import ValidationError
from django.db import models


class Solicitud(models.Model):
    TIPO_ACADEMICA = "academica"
    TIPO_ADMINISTRATIVA = "administrativa"
    TIPO_TECNICA = "tecnica"
    TIPO_OTRA = "otra"

    TIPOS_SOLICITUD = [
        (TIPO_ACADEMICA, "Académica"),
        (TIPO_ADMINISTRATIVA, "Administrativa"),
        (TIPO_TECNICA, "Técnica"),
        (TIPO_OTRA, "Otra"),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=30)
    correo_electronico = models.EmailField()
    telefono_contacto = models.PositiveBigIntegerField()
    tipo_solicitud = models.CharField(max_length=20, choices=TIPOS_SOLICITUD)
    asunto = models.CharField(max_length=120)
    descripcion_detallada = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to="solicitudes/", blank=True, null=True)

    class Meta:
        ordering = ["-fecha_solicitud", "nombre_solicitante"]
        verbose_name = "solicitud"
        verbose_name_plural = "solicitudes"

    def clean(self):
        super().clean()
        if self.fecha_solicitud and self.fecha_solicitud > date.today():
            raise ValidationError(
                {"fecha_solicitud": "La fecha de la solicitud no puede estar en el futuro."}
            )

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.get_tipo_solicitud_display()}"

# Create your models here.
